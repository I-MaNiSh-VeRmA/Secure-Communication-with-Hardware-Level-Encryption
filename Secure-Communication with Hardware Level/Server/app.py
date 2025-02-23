from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import json  # Ensure json is imported for serialization

app = Flask(__name__)

# Database connection setup
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",        # Or use server's IP address
            user="root",             # Replace with your MySQL username
            password="root",         # Replace with your MySQL password
            database="sensor_data"   # Database name
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None
    
    
@app.route('/api/get_data', methods=['GET'])
def get_users():
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM data")  # Replace with your table name
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({"error": f"Database query error: {e}"}), 500
    finally:
        cursor.close()
        connection.close()
           
@app.route('/api/store_data', methods=['POST'])
def store_data():
    # Parse incoming JSON data from request
    data = request.get_json()
    
    # Check for missing or invalid fields in the incoming data
    if 'data' not in data:
        return jsonify({"error": "Invalid input data"}), 400

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    encrypted_data = data['data']
    
    # Establish connection to the database
    connection = get_db_connection()

    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        # Prepare to insert data into MySQL
        cursor = connection.cursor()
        
        # Assuming encrypted_data is in JSON format, ensure it's serialized
        encrypted_data_json = json.dumps(encrypted_data)  # Convert encrypted data to JSON string

        query = "INSERT INTO data (timestamp, encrypted_data) VALUES (%s, %s)"
        cursor.execute(query, (timestamp, encrypted_data_json))  # Insert data into table
        connection.commit()
        cursor.close()

        return jsonify({"message": "Data stored successfully"}), 200
    except Error as e:
        # Handle database errors
        return jsonify({"error": f"Database error: {e}"}), 500
    finally:
        # Close database connection
        connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask server on all available IPs, port 5000

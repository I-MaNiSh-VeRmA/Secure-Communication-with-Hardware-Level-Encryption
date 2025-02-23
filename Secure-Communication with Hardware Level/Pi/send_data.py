import requests
import time
import json
import random
from datetime import datetime

# URL of your Flask server's API endpoint
url = "http://192.168.29.252:5000/api/store_data"  # Replace with the actual IP of the server

# Function to read the encrypted data from a local file

# Function to send data to the Flask server's API
def send_data_to_api(encrypted_data):
    # Generate a timestamp for the current time

    # Prepare the payload to send (id, timestamp, and encrypted data as JSON)
    payload = {
        'data': encrypted_data  # The encrypted data
    }

    try:
        # Send a POST request to the Flask server
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print(f"Data sent successfully")
        else:
            print(f"Failed to send data. Server responded with: {response.status_code} - {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")

# Example usage: send encrypted data every 5 seconds
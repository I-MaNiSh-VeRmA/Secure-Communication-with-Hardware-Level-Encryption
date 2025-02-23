import requests
import decrypt
from decrypt import aes_key

def fetch_data(aes_key):
    # Replace with the actual URL of your API
    api_url = "http://192.168.76.127:5000/api/get_data"

    try:
        # Send a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            dataResponse = response.json()  # Parse JSON response
            print("Data fetched successfully:")
            for data in dataResponse:
                decrypt_data = decrypt.decrypt_data(data['encrypted_data'], aes_key)
                print(f"ID: {data['id']}, Timestamp: {data['timestamp']}, Encrypted_Data: {decrypt_data}")
        else:
            print(f"Failed to fetch users. Status code: {response.status_code}")
            print(f"Error message: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_data(aes_key=aes_key)        

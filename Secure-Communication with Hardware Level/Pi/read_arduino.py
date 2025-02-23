import serial
import json
import time


# arduino_port = "/dev/ttyACM0"  # Update this if needed
arduino_port = "COM5"

baud_rate = 9600               # Match the baud rate in the Arduino code

def read_arduino():
    try:
        with serial.Serial(arduino_port, baud_rate, timeout=1) as ser:
            print("Collecting data. Press Ctrl+C to stop.")
            while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()  # Remove leading/trailing spaces and line breaks
                    print(line)  # Print the raw data to the terminal

                    try:
                        # Parse the JSON data
                        data = json.loads(line)

                        # Print the parsed data
                        print(f"Timestamp: {data['timestamp']}")
                        print(f"Distance: {data['distance']} cm")
                        print(f"Gas Concentration: {data['gas_concentration']} %")
                        print(f"Motion: {data['motion']}")
                        print(f"Temperature: {data['temperature']} C")
                        return data
                    except json.JSONDecodeError:
                        print("Error decoding JSON data.")

    except KeyboardInterrupt:
        print("Data collection stopped.")
    except Exception as e:
        print(f"Error: {e}")

import serial
import json

def collect_vitals_from_robot():
    try:
        # Replace 'COM3' with the appropriate port and 9600 with your baud rate
        with serial.Serial('COM3', 9600, timeout=1) as ser:
            raw_data = ser.readline().decode('utf-8').strip()
            vitals = json.loads(raw_data)  # Expecting JSON data from the robot
            return vitals
    except Exception as e:
        print(f"Error collecting vitals: {e}")
        return None

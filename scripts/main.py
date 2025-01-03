import time
from collect_vitals import collect_vitals_from_robot
from ai_prediction import ai_predict
from upload_to_cloud import upload_to_cloud

def main():
    patient_id = "Patient_001"
    while True:
        vitals = collect_vitals_from_robot()
        if vitals:
            print("Collected Vitals:", vitals)
            predictions = ai_predict(vitals)
            print("AI Predictions:", predictions)
            upload_to_cloud(patient_id, vitals, predictions)
        else:
            print("No data collected from the robot.")
        time.sleep(5)  # Wait for 5 seconds before the next iteration

if __name__ == "__main__":
    main()

import requests

CLOUD_ENDPOINT = "https://your-cloud-endpoint.com/api/upload"

def upload_to_cloud(patient_id, vitals, predictions):
    payload = {
        "patient_id": patient_id,
        "vitals": vitals,
        "predictions": predictions,
        "timestamp": "2025-01-03T12:00:00Z"
    }
    try:
        response = requests.post(CLOUD_ENDPOINT, json=payload)
        if response.status_code == 200:
            print("Data uploaded successfully.")
        else:
            print(f"Failed to upload data: {response.status_code}")
    except Exception as e:
        print(f"Error uploading to cloud: {e}")

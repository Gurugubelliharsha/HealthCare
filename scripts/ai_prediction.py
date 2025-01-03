def ai_predict(vitals):
    predictions = {}
    try:
        if vitals["Temperature (°C)"] > 38:
            predictions["Condition"] = "Fever"
            predictions["Action"] = "Administer paracetamol"
        if vitals["Oxygen Saturation (%)"] < 92:
            predictions["Condition"] = "Hypoxia"
            predictions["Action"] = "Provide supplemental oxygen"
        if vitals["Heart Rate (bpm)"] > 100:
            predictions["Condition"] = "Tachycardia"
            predictions["Action"] = "Monitor and consider beta-blockers"
        return predictions if predictions else {"Condition": "Normal", "Action": "No action required"}
    except KeyError as e:
        print(f"Missing data in vitals: {e}")
        return {"Condition": "Unknown", "Action": "Unable to predict"}

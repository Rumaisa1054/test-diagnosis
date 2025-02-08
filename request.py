import requests

# Define the API URL (Change if hosted remotely)
API_URL = "http://127.0.0.1:5000/predict"

# Sample medical data for prediction
data = {
    "Glucose": 18.395,  # 1
    "Cholesterol": 269.483,  # 2
    "Hemoglobin": 770.933,  # 3
    "Platelets": 876.474,  # 4
    "White Blood Cells": 658.963,  # 5
    "Red Blood Cells": 192.013,  # 6
    "Hematocrit": 22.082,  # 7
    "Mean Corpuscular Volume": 670.047,  # 8
    "Mean Corpuscular Hemoglobin": 777.337,  # 9
    "Mean Corpuscular Hemoglobin Concentration": 696.853,  # 10
    "Insulin": 75.699,  # 11
    "BMI": 5.320,  # 12
    "Systolic Blood Pressure": 979.231,  # 13
    "Diastolic Blood Pressure": 831.999,  # 14
    "Triglycerides": 678.508,  # 15
    "HbA1c": 518.805,  # 16
    "LDL Cholesterol": 261.473,  # 17
    "HDL Cholesterol": 407.381,  # 18
    "ALT": 114.373,  # 19
    "AST": 344.636,  # 20
    "Heart Rate": 367.260,  # 21
    "Creatinine": 258.957,  # 22
    "Troponin": 285.188,  # 23
    "C-reactive Protein": 979.383  # 24
}



# Send POST request to Flask API
response = requests.post(API_URL, json=data)

D = ["Diabetes","Anemia","Thalasse","Heart Disease","Healthy","Thromboc"]
# Print response
if response.status_code == 200:
    print("Prediction:", D[response.json()['disease_prediction'][0]])
else:
    print("Error:", response.json())

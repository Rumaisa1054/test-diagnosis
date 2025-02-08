import pickle
import numpy as np
import sklearn
from flask import Flask, request, jsonify

# Load the model
with open("tree.pkl", "rb") as f:
    model = pickle.load(f)

# Define the Flask app
app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON request data
        data = request.get_json()

        # Define expected features
        expected_features = [
            "Glucose", "Cholesterol", "Hemoglobin", "Platelets", "White Blood Cells",
            "Red Blood Cells", "Hematocrit", "Mean Corpuscular Volume", "Mean Corpuscular Hemoglobin",
            "Mean Corpuscular Hemoglobin Concentration",
            "Insulin","BMI", "Systolic Blood Pressure", "Diastolic Blood Pressure", "Triglycerides", "HbA1c", "LDL Cholesterol",
            "HDL Cholesterol", "ALT", "AST", "Heart Rate", "Creatinine", "Troponin", "C-reactive Protein"
        ]

        # Extract features from request
        features = [data.get(feature, 0) for feature in expected_features]  # Default to 0 if missing

        # Convert to numpy array and reshape for model
        features_array = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features_array)

        # Return JSON response
        return jsonify({"disease_prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
#{"Glucose": 110,"Cholesterol": 190,"Hemoglobin": 13.5,"Platelets": 250000,"White Blood Cells": 7000,"Red Blood Cells": 5.2,"Hematocrit": 42,"Mean Corpuscular Volume": 90,"Mean Corpuscular Hemoglobin": 30,"Mean Corpuscular Hemoglobin Concentration": 33,"Triglycerides": 150,"HbA1c": 5.8,"LDL Cholesterol": 120,"HDL Cholesterol": 50,"ALT": 25,"AST": 20,"Heart Rate": 72,"Creatinine": 1.0,"Troponin": 0.01,"C-reactive Protein": 3.0}

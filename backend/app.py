from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "loan_model.pkl")
model = pickle.load(open(model_path, "rb"))

@app.route("/")
def home():
    return "Loan Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([[
        data['gender'],
        data['married'],
        data['dependents'],
        data['education'],
        data['self_employed'],
        data['income'],
        data['co_income'],
        data['loan_amount'],
        data['loan_term'],
        data['credit'],
        data['area']
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return jsonify({
        "prediction": int(prediction),
        "probability": float(probability)
    })

if __name__ == "__main__":
    app.run(debug=True)
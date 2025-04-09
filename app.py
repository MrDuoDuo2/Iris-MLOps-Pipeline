# app.py (Flask API)
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model/iris_classifier.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = pd.DataFrame([data])
    prediction = model.predict(features)[0]
    return jsonify({"class": int(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
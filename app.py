# app.py (Flask API)
from flask import Flask, request, jsonify
import joblib
import pandas as pd
from prometheus_client import start_http_server, Counter

app = Flask(__name__)
model = joblib.load("model/iris_classifier.joblib")
REQUEST_COUNT = Counter('api_call_total', 'Total API calls')
IRIS_TARGET_NAME_LIST=['setosa', 'versicolor', 'virginica']
@app.route('/predict', methods=['POST'])
def predict():
    REQUEST_COUNT.inc()
    data = request.json
    features = pd.DataFrame([data])

    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0]

    return jsonify({"class": int(prediction),
                    "class_name":IRIS_TARGET_NAME_LIST[prediction],
                    "probabilities": {                 # 所有类别概率
                        "cls": float(prob) for cls, prob in zip(model.classes_, proba)
                    }})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
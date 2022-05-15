from flask import Flask, request, jsonify

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

def scale(payload):
    scaler = StandardScaler.fit(payload)
    return scaler.transform(payload)

@app.route("/")
def home():
    return "<h3>Welcome to the home page of my prediction container!</h3>"


@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
    input looks like:
        {
            "CHAS": {"0": 0},
            "RM": {"0": 6.575},
            "TAX": {"0": 296.0},
            "PTRATIO":{"0": 15.3},
            "B": {"0": 396.9},
            "LSTAT": {"0": 4.98}
        }
    result looks like:
    { "prediction": [ 20.35373177134412 ] }
    """
    clf = joblib.load("boston_housing_prediction.joblib")
    json_payload = request.json
    inference_payload = pd.DataFrame(json_payload)
    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    return jsonify({'prediction': prediction})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
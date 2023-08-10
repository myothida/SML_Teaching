import numpy as np
from flask import Flask, request
from condoPrice_predict import make_prediction

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Condo Price Prediction API</h1>"
        "</body>"
        "</html>"
    )
    return body

@app.route("/predict", methods=["POST"])
def predict():
    data_json = request.get_json()
  
    num_bedrooms = data_json["bedrooms"]
    area_sq_cm = data_json["Area"]
    num_bathrooms = data_json["bathrooms"]

    data = np.array([[num_bedrooms, area_sq_cm, num_bathrooms]])
    predictions = make_prediction(data)
  
    return str(predictions)

if __name__ == "__main__":
    app.run()

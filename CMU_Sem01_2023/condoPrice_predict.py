import joblib
import pandas as pd

model = joblib.load("CNX_BestModel.pkl")

def make_prediction(inputs):
    """
    Make a prediction using the trained model
    """
    inputs_df = pd.DataFrame(
        inputs,
        columns=["bedrooms", "Area", "bathrooms"]
        )
    predictions = model.predict(inputs_df)
  
    return predictions
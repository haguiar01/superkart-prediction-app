import joblib
import numpy as np
import pandas as pd
import os
from flask import Flask, request, jsonify

# define file name and location (relative to container root)
# allow for different models to be used by receiving the model name from environment
DEFAULT_MODEL_NAME = "superkart_adaboost_model_v1_0.joblib"
MODEL_PATH = f'models/{os.getenv("MODEL_NAME", DEFAULT_MODEL_NAME)}'

# initialize flask app with a name
superkart_api = Flask("SuperKart Sales Prediction")

# load the trained model
default_model = joblib.load(f'models/{DEFAULT_MODEL_NAME}')

def get_model(name):
    if name == None or name == DEFAULT_MODEL_NAME:
        return default_model

    # safely loads the model inside the individual worker process memory
    return joblib.load(MODEL_PATH)

# route for the home page
@superkart_api.get('/')
def home():
    return "Welcome to the SuperKart Sales Price Prediction API!"

# endpoint to predict sales for a single entry
@superkart_api.post('/v1/predict')
def predict():
    # get data from the request
    data = request.get_json()

    # prepare data for model
    input_data = pd.DataFrame([{
      'Product_Weight': data['Product_Weight'],
      'Product_Sugar_Content': data['Product_Sugar_Content'],
      'Product_Allocated_Area': data['Product_Allocated_Area'],
      'Product_Type': data['Product_Type'],
      'Product_MRP': data['Product_MRP'],
      'Store_Size': data['Store_Size'],
      'Store_Location_City_Type': data['Store_Location_City_Type'],
      'Store_Type': data['Store_Type'],
      'Store_Age': data['Store_Age']
    }])

    # use the model to make the prediction
    prediction = get_model(data['Model_Name']).predict(input_data).tolist()[0]

    # return the predicted value in API response
    return jsonify({'Sales': prediction})

# Run the Flask app in debug mode
if __name__ == '__main__':
    superkart_api.run(debug=True)

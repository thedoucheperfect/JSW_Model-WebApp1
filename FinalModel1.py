import joblib
import numpy as np
import pandas as pd

# Load the saved model and scaler
model_path = 'energy_models/xgboost_model.joblib'
scaler_path = 'energy_models/standard_scaler.joblib'
feature_names_path = 'energy_models/feature_names.joblib'


model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
feature_names = joblib.load(feature_names_path)

def predict_power(input_thick, input_width, ip_wt, thickness_actual, number_of_passes):
    # Create a DataFrame with the input features
    input_data = pd.DataFrame([[input_thick, input_width, ip_wt, thickness_actual, number_of_passes]],
                              columns=feature_names)

    # Scale the input features
    scaled_features = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(scaled_features)

    return round(prediction[0], 2)

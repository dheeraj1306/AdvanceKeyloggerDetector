import joblib 
import numpy as np

# Load pre-trained anomaly detection model
model = joblib.load("model.pkl")

def analyze_process(process_data):
    process_data = np.array(process_data).reshape(1, -1)
    prediction = model.predict(process_data)
    return prediction == -1  

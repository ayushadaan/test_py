# predictor/predict.py
import joblib
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), 'model', 'fitness_model.pkl')
model = joblib.load(model_path)

def predict_fitness(data):
    features = np.array([
        data["blood_pressure"],
        data["blood_sugar"],
        data["heart_rate"],
        data["injury"],
        data["age"]
    ]).reshape(1, -1)
    result = model.predict(features)
    return bool(result[0])

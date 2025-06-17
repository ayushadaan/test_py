# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# 1. Sample dataset
data = pd.DataFrame([
    {"blood_pressure": 120, "blood_sugar": 90, "heart_rate": 70, "injury": 0, "age": 25, "fit": 1},
    {"blood_pressure": 150, "blood_sugar": 180, "heart_rate": 100, "injury": 1, "age": 32, "fit": 0},
    {"blood_pressure": 130, "blood_sugar": 95, "heart_rate": 72, "injury": 0, "age": 22, "fit": 1},
    {"blood_pressure": 160, "blood_sugar": 200, "heart_rate": 110, "injury": 1, "age": 35, "fit": 0},
    {"blood_pressure": 110, "blood_sugar": 80, "heart_rate": 65, "injury": 0, "age": 20, "fit": 1}
])

# 2. Features and target
X = data.drop("fit", axis=1)
y = data["fit"]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Save model to predictor/model/fitness_model.pkl
output_dir = os.path.join("predictor", "model")
os.makedirs(output_dir, exist_ok=True)  # Create folder if it doesn't exist

model_path = os.path.join(output_dir, "fitness_model.pkl")
joblib.dump(model, model_path)

print(f"✅ Model trained and saved to: {model_path}")

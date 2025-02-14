import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# Extract features (CPU & Memory Usage)
X = df[['CPU_Usage', 'Memory_Usage']].values

# Train Isolation Forest Model
model = IsolationForest(n_estimators=100, contamination=0.15, random_state=42)
model.fit(X)

# Save the trained model
joblib.dump(model, "model.pkl")
print("[SUCCESS] Model trained and saved as model.pkl")

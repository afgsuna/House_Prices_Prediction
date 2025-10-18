# src/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from joblib import dump
from pathlib import Path
import json
import math

DATA = Path(__file__).resolve().parents[1] / "data/processed/train_processed.csv"
MODEL_OUT = Path(__file__).resolve().parents[1] / "model/model.joblib"
COLS_OUT = Path(__file__).resolve().parents[1] / "model/columns.json"

print("🔹 Loading processed data...")
df = pd.read_csv(DATA)

# Separate features and target
X = df.drop(columns=["SalePrice"], errors='ignore')
y = df["SalePrice"]

# Keep numeric columns only
X = X.select_dtypes(include=["number"]).fillna(0)

# Save numeric columns for API
COLS_OUT.parent.mkdir(parents=True, exist_ok=True)
with open(COLS_OUT, "w") as f:
    json.dump(list(X.columns), f)

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
print("🔹 Training model...")
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
r2 = r2_score(y_test, preds)
rmse = math.sqrt(mean_squared_error(y_test, preds))
print(f"✅ Model trained. R²: {r2:.4f}, RMSE: {rmse:.2f}")

# Save model
dump(model, MODEL_OUT)
print(f"💾 Saved model to {MODEL_OUT}")

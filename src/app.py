# src/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from joblib import load
from pathlib import Path
import json

# Load model
MODEL_PATH = Path(__file__).resolve().parents[1] / "model/model.joblib"
model = load(MODEL_PATH)

# Load column order
COLS_PATH = Path(__file__).resolve().parents[1] / "model/columns.json"
with open(COLS_PATH) as f:
    model_columns = json.load(f)

# FastAPI app
app = FastAPI(title="House Prices Prediction API", version="0.1.0")

# Input schema (only a few key features for simplicity)
class InputData(BaseModel):
    OverallQual: int
    GrLivArea: float
    YearBuilt: int

@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])
    # Fill missing columns with 0
    for col in model_columns:
        if col not in df.columns:
            df[col] = 0
    # Reorder columns to match training
    df = df[model_columns]
    pred = model.predict(df)[0]
    return {"predicted_price": float(pred)}

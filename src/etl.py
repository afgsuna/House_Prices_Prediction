# src/etl.py
import pandas as pd
from pathlib import Path

RAW = Path(__file__).resolve().parents[1] / "data/raw/train.csv"
PROCESSED = Path(__file__).resolve().parents[1] / "data/processed/train_processed.csv"

def run():
    print("🔹 Loading raw data...")
    df = pd.read_csv(RAW)
    print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")

    # Drop columns with too many missing values
    df = df.dropna(axis=1, thresh=0.6 * len(df))

    # Fill numeric missing values with median
    num_cols = df.select_dtypes(include=["number"]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # Fill categorical missing values with "missing"
    cat_cols = df.select_dtypes(include=["object"]).columns
    df[cat_cols] = df[cat_cols].fillna("missing")

    # Save processed dataset
    PROCESSED.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED, index=False)
    print(f"✅ Saved processed data to {PROCESSED}")

if __name__ == "__main__":
    run()

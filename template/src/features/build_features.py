"""
src.features.build_features

Script to build and transform features for {{ project_name }}.

- Reads processed data, outputs feature matrices for ML models.
- Designed to be run as a script (python -m src.features.build_features).
- Extend each function with your project-specific logic.

Pro tip: Use config/settings.py for paths and params, not hardcoded values.
"""

import pandas as pd
from pathlib import Path
from src.config.settings import settings

PROCESSED_DATA_DIR = Path("data/processed")
FEATURES_DATA_DIR = Path("data/features")


def load_processed_data():
    """
    Load processed/cleaned data for feature engineering.
    """
    data_path = PROCESSED_DATA_DIR / "cleaned.csv"
    if not data_path.exists():
        raise FileNotFoundError(f"No processed data at {data_path}")
    return pd.read_csv(data_path)


def engineer_features(df):
    """
    Create/transform features for ML models.
    Extend this function with your logic.
    """
    # Example: create dummy variable
    df["feature_one"] = df.select_dtypes(include="number").sum(axis=1)
    # Add more feature engineering here
    return df


def save_features(df):
    """
    Save the feature matrix to FEATURES_DATA_DIR.
    """
    FEATURES_DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = FEATURES_DATA_DIR / "features.csv"
    df.to_csv(out_path, index=False)
    print(f"Feature matrix saved to {out_path}")


def main():
    print(f"Loading processed data from {PROCESSED_DATA_DIR}")
    df = load_processed_data()
    print("Engineering features...")
    df_features = engineer_features(df)
    save_features(df_features)


if __name__ == "__main__":
    main()
# This script is designed to be run as a module, e.g.: python -m src.features.build_features
# Ensure you have the necessary directories created before running this script.
# You can run this script directly or integrate it into your ML pipeline.

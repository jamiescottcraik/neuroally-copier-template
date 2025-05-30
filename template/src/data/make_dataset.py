"""
src.data.make_dataset

Script to create, clean, and split datasets for {{ project_name }}.

- Use this as the entry point for all data processing.
- Designed to be run as a script (python -m src.data.make_dataset).
- Reads raw data, outputs processed data to /data/processed.
- Extend functions for your actual use case.

Pro tip: Use config/settings.py for all paths and params.
"""

import os
from pathlib import Path
import pandas as pd  # If you’re not using pandas, swap for your lib of choice

from src.config.settings import settings

RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")


def load_raw_data():
    """
    Load raw data from RAW_DATA_DIR.
    Extend this function for your real data sources.
    """
    # Example: loading a CSV file
    data_path = RAW_DATA_DIR / "input.csv"
    if not data_path.exists():
        raise FileNotFoundError(f"No raw data found at {data_path}")
    return pd.read_csv(data_path)


def clean_data(df):
    """
    Clean/process the raw dataframe.
    Extend with your project-specific logic.
    """
    # Example: drop NA, filter, type-cast, etc.
    df = df.dropna()
    # Add more cleaning steps as needed
    return df


def save_processed_data(df):
    """
    Save the cleaned dataframe to PROCESSED_DATA_DIR.
    """
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DATA_DIR / "cleaned.csv"
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")


def main():
    print(f"Loading raw data from {RAW_DATA_DIR}")
    df = load_raw_data()
    print("Cleaning data...")
    df_clean = clean_data(df)
    save_processed_data(df_clean)


if __name__ == "__main__":
    main()
# This script is designed to be run as a module, e.g., python -m src.data.make_dataset

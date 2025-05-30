"""
src/main.py

Robust entry point for running your AI/data pipeline.
Handles config, errors, CLI args, and customizable plotting.
"""

import sys
import argparse
from pathlib import Path

# --- Config import ---
try:
    from src.config.settings import (
        config,
    )  # config must be a dict with DATA_PATH, MODEL_PATH keys
except ImportError:
    config = {}

from src.data.make_dataset import load_data
from src.features.build_features import build_features
from src.models.predict_model import load_model, predict
from src.visualization import plot_data


def parse_args():
    parser = argparse.ArgumentParser(description="Run the ML/data pipeline")
    parser.add_argument(
        "--data_path",
        type=str,
        default=config.get("DATA_PATH", "data/raw/data.csv"),
        help="Path to input data file",
    )
    parser.add_argument(
        "--model_path",
        type=str,
        default=config.get("MODEL_PATH", "models/model.pkl"),
        help="Path to model file",
    )
    parser.add_argument(
        "--plot_x",
        type=str,
        default=None,
        help="Column for x axis in plots",
    )
    parser.add_argument(
        "--plot_y",
        type=str,
        default=None,
        help="Column for y axis in plots",
    )
    parser.add_argument(
        "--plot_kind",
        type=str,
        default="line",
        help="Plot kind (line, bar, scatter, etc.)",
    )
    parser.add_argument(
        "--save_plot",
        type=str,
        default=None,
        help="Path to save plot (optional)",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Don't show plots interactively (for CI/production runs)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        # --- 1. Load Data ---
        print(f"Loading data from: {args.data_path}")
        df = load_data(path=args.data_path)
        print(f"Data loaded: {df.shape}")

        # --- 2. Build Features ---
        print("Building features...")
        X, y = build_features(df)
        print(f"Features built: X shape={X.shape}, y shape={y.shape}")

        # --- 3. Load Model and Predict ---
        print(f"Loading model from: {args.model_path}")
        model = load_model(path=args.model_path)
        print("Model loaded. Making predictions...")
        y_pred = predict(model, X)
        print("Prediction complete.")

        # --- 4. Visualize Results ---
        plot_x = (
            args.plot_x
            if args.plot_x
            else (
                X.columns[0] if hasattr(X, "columns") and len(X.columns) > 0 else None
            )
        )
        plot_y = (
            args.plot_y if args.plot_y else (y.name if hasattr(y, "name") else None)
        )

        if not plot_x or not plot_y:
            print("No valid plot_x or plot_y specified. Skipping plot.")
        else:
            print(f"Plotting: x='{plot_x}', y='{plot_y}', kind='{args.plot_kind}'")
            plot_data(
                df,
                x=plot_x,
                y=plot_y,
                kind=args.plot_kind,
                title="Sample Plot",
                save_path=args.save_plot,
                show=not args.headless,
            )
            if args.save_plot:
                print(f"Plot saved to: {args.save_plot}")

    except Exception as e:
        print(f"Error during pipeline run: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
# This is the main entry point for the AI/data pipeline.
# It handles loading data, building features, making predictions,
# and visualizing results with customizable plotting options.
# It also supports command-line arguments for flexibility.
# Ensure this script is run as the main module.
# This allows for easy integration into larger workflows or CI/CD pipelines.
# The script is designed to be robust and user-friendly,
# with clear error handling and informative output.
# It can be extended with additional features or modified
# to suit specific use cases or workflows.

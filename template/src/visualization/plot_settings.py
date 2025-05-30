"""
src/visualization/plot_settings.py

Central place for plot style, formatting, and config.
Call `set_plot_style()` at the start of every notebook or script.
"""

import matplotlib.pyplot as plt


def set_plot_style():
    """Set global style for matplotlib plots."""
    plt.style.use("ggplot")  # Or 'seaborn-v0_8', 'dark_background', etc.

    # Consistent font and figure sizes
    plt.rcParams.update(
        {
            "figure.figsize": (10, 6),
            "axes.titlesize": 18,
            "axes.labelsize": 14,
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "legend.fontsize": 12,
            "axes.grid": True,
            "grid.linestyle": "--",
            "grid.alpha": 0.7,
            "axes.facecolor": "#f7f7f7",
            "figure.facecolor": "#f7f7f7",
            "axes.edgecolor": "#333333",
        }
    )


# Optionally, add similar for plotly if you use it
try:
    import plotly.io as pio

    def set_plotly_style():
        """Set default Plotly theme."""
        pio.templates.default = "plotly_white"
except ImportError:
    pass
# Ensure this module is imported in your main visualization module

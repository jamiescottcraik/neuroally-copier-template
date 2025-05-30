"""
src/visualization/visualize.py

Reusable plotting utilities for data science, ML, and reporting.
"""

import matplotlib.pyplot as plt


def plot_data(
    df,
    x=None,
    y=None,
    kind="line",
    title="Data Plot",
    xlabel=None,
    ylabel=None,
    grid=True,
    save_path=None,
    show=True,
    **kwargs,
):
    """
    Plot pandas DataFrame columns easily, with error handling and option to save.

    Args:
        df (pd.DataFrame): Data to plot.
        x (str, optional): Column name for X axis.
        y (str or list, optional): Column name(s) for Y axis.
        kind (str): 'line', 'bar', 'hist', etc.
        title (str): Plot title.
        xlabel (str, optional): X axis label.
        ylabel (str, optional): Y axis label.
        grid (bool): Show grid.
        save_path (str, optional): If set, save plot to this file.
        show (bool): If True, display the plot.
        **kwargs: Passed to pandas.DataFrame.plot()
    """
    # Error handling
    cols = df.columns
    if x and x not in cols:
        raise ValueError(f"Column '{x}' not in DataFrame")
    if y:
        missing = [col for col in ([y] if isinstance(y, str) else y) if col not in cols]
        if missing:
            raise ValueError(f"Column(s) {missing} not in DataFrame")

    ax = df.plot(x=x, y=y, kind=kind, grid=grid, figsize=(10, 6), **kwargs)
    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else (x if x else ""))
    ax.set_ylabel(ylabel if ylabel else (y if y else ""))
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close()


def plot_predictions(
    y_true,
    y_pred,
    title="Predictions vs. Actuals",
    xlabel="Actual",
    ylabel="Predicted",
    save_path=None,
    show=True,
):
    """
    Quick scatter plot for regression predictions.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(y_true, y_pred, alpha=0.7)
    plt.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)], "r--")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close()


# Optional: add a plotly version if you use plotly
try:
    import plotly.express as px

    def plot_data_plotly(
        df,
        x=None,
        y=None,
        kind="line",
        title="Data Plot",
        save_path=None,
        show=True,
        **kwargs,
    ):
        """
        Simple Plotly wrapper for DataFrame plotting, with save and error handling.
        """
        if x and x not in df.columns:
            raise ValueError(f"Column '{x}' not in DataFrame")
        if y:
            missing = [
                col
                for col in ([y] if isinstance(y, str) else y)
                if col not in df.columns
            ]
            if missing:
                raise ValueError(f"Column(s) {missing} not in DataFrame")

        if kind == "line":
            fig = px.line(df, x=x, y=y, title=title, **kwargs)
        elif kind == "bar":
            fig = px.bar(df, x=x, y=y, title=title, **kwargs)
        elif kind == "scatter":
            fig = px.scatter(df, x=x, y=y, title=title, **kwargs)
        else:
            raise ValueError(f"Plotly kind '{kind}' not supported.")
        if save_path:
            fig.write_image(save_path)
        if show:
            fig.show()
except ImportError:
    pass
# If plotly is not installed, the plot_data_plotly function will not be available.
# This allows the rest of the code to run without plotly.
# This is useful if you want to keep the code lightweight and only use plotly when needed.
# You can install plotly with `pip install plotly` if you want to use it.

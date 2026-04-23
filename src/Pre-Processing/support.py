#
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
#
def BoxplotTable(df,n_cols,name): 
    #
    columns_to_plot = df.columns
    #
    n_rows = (len(columns_to_plot) + n_cols - 1) // n_cols
    #
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(3.2 * n_cols, 2.8 * n_rows))
    axes = axes.flatten()
    #
    for ax, col in zip(axes, columns_to_plot):
        df.boxplot(column=col, ax=ax)
        #
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        medium_lower = q1 - 3 * iqr
        medium_upper = q3 + 3 * iqr
        heavy_lower = q1 - 10 * iqr
        heavy_upper = q3 + 10 * iqr
        ax.axhline(medium_lower, color="yellow", linewidth=1)
        ax.axhline(medium_upper, color="yellow", linewidth=1)
        ax.axhline(heavy_lower, color="red", linestyle="--", linewidth=1)
        ax.axhline(heavy_upper, color="red", linestyle="--", linewidth=1)
        #
        ax.set_title(col, fontsize=9)
        ax.tick_params(axis="x", labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
    #
    for ax in axes[len(columns_to_plot):]:
        ax.set_visible(False)
    #
    legend_handles = [
        Line2D([0], [0], color="yellow", linewidth=1, label="Medium outlier threshold (3 x IQR)"),
        Line2D([0], [0], color="red", linestyle="--", linewidth=1, label="Heavy outlier threshold (10 x IQR)"),
    ]
    fig.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.98),
        ncol=2,
        frameon=False,
        fontsize=9,
    )
    fig.suptitle(name, y=1.03, fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    plt.show()
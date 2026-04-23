#loading libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
#function to create boxplots for all features in a dataframe with outlier thresholds
def BoxplotTable(df,n_cols,name): 
    #getting the column names of the dataframe
    columns_to_plot = df.columns
    #calcualting amount of needed rows to fit all the boxplots (based on how many columns are availible)
    n_rows = (len(columns_to_plot) + n_cols - 1) // n_cols
    #creating the subplots for the boxplots to fill
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(3.2 * n_cols, 2.8 * n_rows))
    axes = axes.flatten()
    #iterating through features to create boxplots for each
    for ax, col in zip(axes, columns_to_plot):
        #creating current boxplot
        df.boxplot(column=col, ax=ax)
        skew_value = df[col].dropna().skew()#calculating the skewness of the current feature to include it in the boxplot title
        #calculating outlier thresholds
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
        #setting boxplot descriptions
        ax.set_title(f"{col}\nskew={skew_value:.2f}", fontsize=9)#adding the skewness
        ax.tick_params(axis="x", labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
    #setting the remaining subplots to invisible if there are more subplots than features (as the grid of boxplots was generated from column/row numbers, but not all subplots are needed if the number of features is not a perfect multiple of this number)
    for ax in axes[len(columns_to_plot):]:
        ax.set_visible(False)
    #adding a legend for the outlier thresholds
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
    #setting the overall title for the figure
    fig.suptitle(name, y=1.03, fontsize=12)
    #setting the layout of the figure to prevent overlap between subplots and title
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    #displaying the boxplots
    plt.show()
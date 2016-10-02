import matplotlib.pyplot as plt
import pandas as pd
import os

plt.style.use("ggplot")

def create_graph(dataframe, x_col_index, y_col_index, column_names):
    x_column = column_names[x_col_index]
    y_column = column_names[y_col_index]
    color_column = column_names[0]
    return dataframe.plot.scatter(x=x_column, y=y_column, c=color_column, colormap="RdBu")


def save_graph(plt, filename):
    fig = plt.get_figure()
    fig.savefig(filename)


def clean_data(dataframe):
    result = dataframe.copy()

    # Standardize each column except for the first
    mean = dataframe[dataframe.columns[1:]].mean()
    std = dataframe[dataframe.columns[1:]].std()

    # Only update all but first column
    result[dataframe.columns[1:]] = (result[dataframe.columns[1:]] - mean) / std
    return result

def plot_all_data(df, title, foldername, column_names):
    graph_num = 1
    if not (os.path.exists("graphs/" + foldername)):
        os.mkdir("graphs/" + foldername)
    for x in range(1, len(column_names) - 1):
        for y in range(1, len(column_names)):
            if x == y:
                continue
            plt = create_graph(df, x, y, column_names)
            plt.set_title(title)
            save_graph(plt, "./graphs/"+foldername+"/graph{0}.png".format(graph_num))
            graph_num += 1


if __name__ == "__main__":
    column_names = [
        "Class Label",
        "Number of times pregnant",
        "Plasma glucose concentration",
        "Diastolic blood pressure (mm Hg)",
        "Triceps skin fold thickness (mm)",
        "Insulin (mu U/ml)",
        "Body mas index (kg/m^2)",
        "Diabetes pedigree function",
        "Age (yrs)"
    ]

    # Read Data
    df = pd.read_csv("./diabetes.csv", names=column_names)

    if not(os.path.exists("graphs")):
        os.mkdir("graphs")

    # Plot all the Raw data in pairs of features
    plot_all_data(df, "Raw Data", "raw", column_names)

    # Plot a scatter matrix

    clean_df = clean_data(df)

    # Plot all the Standardized data in pairs of features
    plot_all_data(clean_df, "Standardized Data", "clean", column_names)
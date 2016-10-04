import os


def create_graph(dataframe, x_col_name, y_col_name, label_col_name):
    """
    Create a scatter plot graph and return it
    :param dataframe: Dataframe containing data to plot
    :param x_col_name: Name of the column to plot on the x axis
    :param y_col_name: Name of the column to plot on the y axis
    :param label_col_name: Name of the column which contains the label information
    :return:
    """
    return dataframe.plot.scatter(x=x_col_name, y=y_col_name, c=label_col_name, colormap="RdBu")


def save_graph(plt, filepath):
    """
    Save the given plot to the specified filename
    :param plt: plot to save
    :param filename: filepath to save the plot to
    :return:
    """
    fig = plt.get_figure()
    fig.savefig(filepath)


def plot_all_data(dataframe, title, folder_path, column_names):
    """
    Save all of the 2-pair possible combinations within the given dataframe to the specified folder
    :param dataframe: Dataframe containing data to plot, first column is the label, subsequent are features
    :param title: Title of the plot
    :param folderpath: Path of the folder to save the plots into
    :param column_names: list of columns, first column is the label, subsequent columns are feature names
    :return:
    """
    graph_num = 1
    if not (os.path.exists(folder_path)):
        os.makedirs(folder_path)

    label_col_name = column_names[0]

    for x in range(1, len(column_names) - 1):
        for y in range(1, len(column_names)):
            if x == y:
                continue

            x_col_name = column_names[x]
            y_col_name = column_names[y]
            plt = create_graph(dataframe, x_col_name, y_col_name, label_col_name)
            plt.set_title(title)

            filename = "graph{0}.png".format(graph_num)
            filepath = os.path.join(folder_path, filename)
            save_graph(plt, filepath)
            graph_num += 1
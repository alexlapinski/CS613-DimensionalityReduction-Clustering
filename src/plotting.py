import os


def create_graph(dataframe, x_col_name, y_col_name):
    """
    Create a scatter plot graph and return it

    Since, for the diabetes dataset, we know we have just 2 labels, we can show them each here

    :param dataframe: Dataframe containing data to plot
    :param x_col_name: Name of the column to plot on the x axis
    :param y_col_name: Name of the column to plot on the y axis
    :param label_col_name: Name of the column which contains the label information
    :return:
    """

    # TODO: Allow passed in dictionary of color to labels

    plt = dataframe.loc[-1].plot.scatter(x=x_col_name, y=y_col_name, color="Red", label="-1")
    return dataframe.loc[1].plot.scatter(x=x_col_name, y=y_col_name, color="Blue", label="1", ax=plt)


def save_graph(plt, filepath):
    """
    Save the given plot to the specified filename
    :param plt: plot to save
    :param filename: filepath to save the plot to
    :return:
    """
    fig = plt.get_figure()
    fig.savefig(filepath)


def plot_all_data(dataframe, title, name_prefix, folder_path, column_names):
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

    for x in range(0, len(column_names)):
        for y in range(0, len(column_names)):
            if x == y:
                continue

            x_col_name = column_names[x]
            y_col_name = column_names[y]
            plt = create_graph(dataframe, x_col_name, y_col_name)
            plt.set_title(title)

            filename = "{0}-graph{1}.png".format(name_prefix, graph_num)
            filepath = os.path.join(folder_path, filename)
            save_graph(plt, filepath)
            graph_num += 1
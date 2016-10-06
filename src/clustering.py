import pandas as pd
import numpy as np

def compute_scatter_matrix(dataframe, label):
    num_items = len(dataframe.loc[label])
    return (num_items - 1) * dataframe.loc[label]


def perform_lda(dataframe):
    """
    Perform LDA on binary classified data
    :param dataframe:
    :return:
    """

    # TODO: Right now, we assume multi-class, but the HW only needs for 2 class (which is slightly easier)

    labels = dataframe.index.unique()

    # Compute the mean and standard deviation for each feature, for each label
    means = {label: dataframe.loc[label].mean() for label in labels}

    # Compute Scatter Matricies for each class
    scat_b = {label: compute_scatter_matrix(dataframe, label) for label in labels}

    (mean1 - mean2)T(mean1-mean2)


    # Compute the within scatter matrix
    scat_w = reduce(lambda matrix1, matrix2: matrix1 + matrix2, scat_b.values())

    # Get the inverse
    scat_w = np.linalg.inv(scat_w)

    # Perform eigendecomposition
    evalues, evectors = np.linalg.eig(np.dot(scat_w, scat_b))

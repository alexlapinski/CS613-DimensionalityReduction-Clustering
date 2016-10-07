import data
import numpy as np
import pandas as pd

def perform_pca(dataframe, num_dimensions):
    """
    Perform PCA analysis on the given dataframe
    :param dataframe: The dataframe of source data, first column is the label column
    :param num_dimensions: the number of dimensions to reduce to
    :return:
    """

    # Clean/Standardize the Data
    print "Standardizing Data"
    std_df = data.clean_data(dataframe)

    # Compute the covariance matrix
    print "Computing Covariance Matrix"
    cov_matrix = std_df.cov()

    # Compute Eigenvectors + Eigenvalues of Covariance Matrix
    print "Finding Eigenvalues and Eigenvectors"
    evalues, evectors = np.linalg.eig(cov_matrix)

    # Since evalues are not guarenteed sorted, we need to keep a mapping to the eigenvectors and sort the values
    index = {evalues[i]:i for i in xrange(len(evalues))}

    # sort the evalues highest to lowest
    evalues.sort()
    evalues[:] = evalues[::-1]

    # Pick m<d eigenvectors with highest eigenvalues
    selected_indicies = [index[val] for val in evalues[:num_dimensions]]

    # Build projection matrix
    print "Projecting Data to {0} Dimensions".format(num_dimensions)
    projection_matrix = evectors[:, selected_indicies]

    # Project original dataframe using projection matrix
    new_data = np.dot(std_df, projection_matrix)

    # Preserve the labels
    labels = dataframe.index

    # Return new dataframe
    projected_df = pd.DataFrame(new_data, index=labels)
    projected_df.columns = ["Feature #{0}".format(i) for i in projected_df.columns]
    return projected_df
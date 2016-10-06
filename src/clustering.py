import pandas as pd
import numpy as np
import data
import random
import matplotlib.pyplot as plt
import os
import math
import sys

def distance(pt1, pt2, columns):
    """
    Find the L1 distance between pt1 and pt2. The number of columns in each point must be the same.
    The exact column names must also match. A list of columns must be passed in to only consider those columns when computing distance.
    :param pt1: Source point
    :param pt2: Destination point
    :param columns: A list of columns to use when computing distance, only these columns will be considered
    :return:
    """
    return math.sqrt(sum((pt1[columns] - pt2[columns])**2))

def assign_membership(df, cluster_centers, columns):
    """
    Return a dictionary of clusters to assigned indices
    The key of the dictionary is the index of the cluster in data_indices
    The value is a list of indices of points within the given df
    :param df: DataFrame containing data points
    :param data_indicies: list of indicies which serve as center points
    :param columns: List of column names to consider when computing distance.
    :return:
    """
    membership_df = {ki:[] for ki in xrange(len(cluster_centers))} # Key = point index, Value = Assigned Cluster
    for i in xrange(len(df)):
        min_distance = sys.maxint
        assigned_cluster = -1
        for ki in xrange(len(cluster_centers)):
            pt = cluster_centers[ki]
            dist = distance(pt, df.iloc[i], columns)
            if(dist < min_distance):
                assigned_cluster = ki
                min_distance = dist

        membership_df[assigned_cluster].append(i)

    return membership_df

def kmeans(dataframe, col_1_index, col_2_index, k, output_path, columns, cluster_colors = ['r', 'b']):
    """
    Perform Clustering using K-Means
    :param dataframe:
    :param col_1_index: The index of the first feature to plot
    :param col_2_index: The index of the second feature to plot
    :param k: The k value for k-means
    :param output_path: The path to save the graphs to.
    :param columns: The list of columns to use when computing distance.
    :param cluster_colors: A list of colors to use when displaying clusters in graphs.
    :return:
    """

    # TODO: Make sure code works for any number of features, but only plot 2 features & 2 clusters

    # TODO: Expose parameter to control columns used for computing distance / membership

    # Standardize Data
    std_df = data.clean_data(dataframe)

    # Seed Random Number Generator with '0'
    random.seed(0)

    # Randomly select k data instances and use for initial means
    cluster_centers = [std_df.iloc[random.randrange(0, len(std_df)-1)] for i in xrange(k)]

    # Plot the initial Setup
    #   DataPoints = Red X
    #   Cluster Centers = Blue O

    # Plot the Data Points
    plt.plot(std_df[std_df.columns[col_1_index]], std_df[std_df.columns[col_2_index]], 'rx')

    for cluster_center in cluster_centers:
        plt.plot(cluster_center[cluster_center.index[col_1_index]], cluster_center[cluster_center.index[col_2_index]], 'bo')

    plt.title("Initial Configuration")
    plt.xlabel(std_df.columns[col_1_index])
    plt.ylabel(std_df.columns[col_2_index])
    plt.savefig(os.path.join(output_path, "InitialConfiguration.png"))

    # Assign Membership
    membership = assign_membership(std_df, cluster_centers, columns)
    plt.clf()

    # Plot the clusters
    for cluster in xrange(0, k):
        color = cluster_colors[cluster]
        plt.plot(std_df.iloc[membership[cluster]][std_df.columns[col_1_index]],
                 std_df.iloc[membership[cluster]][std_df.columns[col_2_index]], color + 'x')

    # Plot the means
    for cluster_index in xrange(len(cluster_centers)):
        cluster_center = cluster_centers[cluster_index]
        color = cluster_colors[cluster_index]
        plt.plot(cluster_center[cluster_center.index[col_1_index]], cluster_center[cluster_center.index[col_2_index]], color + 'o')

    plt.title("Initial Assignment")
    plt.xlabel(std_df.columns[col_1_index])
    plt.ylabel(std_df.columns[col_2_index])
    plt.savefig(os.path.join(output_path, "InitialAssignment.png"))

    # Plot initial Cluster Assignments
    #   Cluster 1 = Red
    #   Cluster 2 = Blue
    #   DataPoints = Xs
    #   Cluster centers = Os

    #Plot final cluster assignments
    #   Cluster 1 = Red
    #   Cluster 2 = Blue
    #   DataPoints = Xs
    #   Cluster centers = Os
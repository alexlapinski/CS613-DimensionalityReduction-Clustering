import pandas as pd

column_names = [
        "Number of times pregnant",
        "Plasma glucose concentration",
        "Diastolic blood pressure (mm Hg)",
        "Triceps skin fold thickness (mm)",
        "Insulin (mu U/ml)",
        "Body mas index (kg/m^2)",
        "Diabetes pedigree function",
        "Age (yrs)"
    ]

def read_data(filepath):
    """"
    Read the diabetes csv and return a dataframe
    """
    return pd.read_csv(filepath, names=column_names, index_col=0)


def clean_data(dataframe):
    """
    Standardize a given data frame, exclude the first column (assume it is a label)
    :param dataframe:
    :return:
    """
    result = dataframe.copy()

    # Standardize each column except for the first
    mean = dataframe.mean()
    std = dataframe.std()

    # Only update all but first column
    result = (result - mean) / std
    return result
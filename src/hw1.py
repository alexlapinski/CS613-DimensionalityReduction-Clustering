import matplotlib.pyplot as plt
import argparse
import data
import plotting
from os import path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CS 613 - HW 1 Assignment")
    parser.add_argument("-r", "--plot-raw-data", action="store_true", dest="plot_raw_data",
                        help="Plot and save graphs of the raw data")
    parser.add_argument("-s", "--plot-standardized-data", action="store_true", dest="plot_standardized_data",
                        help="Plot and save graphs of the standardized data")
    parser.add_argument("--style", action="store", dest="style", default="ggplot",
                        help="Set the matplotlib render style (default: ggplot)")
    parser.add_argument("--data", action="store", dest="data_filepath", default="./diabetes.csv",
                        help="Set the filepath of the data csv file. (default: ./diabetes.csv)")
    parser.add_argument("--out", action="store", dest="output_folderpath", default="graph",
                        help="Set the output path of the folder to save graphs (default: graph)")

    args = parser.parse_args()

    plt.style.use(args.style)

    df = data.read_data(args.data_filepath)

    if(args.plot_raw_data):
        plotting.plot_all_data(df, "Raw Data", path.join(args.output_folderpath, "raw"), data.column_names)

    if(args.plot_standardized_data):
        clean_df = data.clean_data(df)
        plotting.plot_all_data(clean_df, "Standardized Data", path.join(args.output_folderpath, "clean"), data.column_names)
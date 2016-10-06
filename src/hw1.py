import matplotlib.pyplot as plt
import argparse
import data
import pca
import plotting
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CS 613 - HW 1 Assignment")
    parser.add_argument("-r", "--plot-raw-data", action="store_true", dest="plot_raw_data",
                        help="Plot and save graphs of the raw data")
    parser.add_argument("-s", "--plot-standardized-data", action="store_true", dest="plot_standardized_data",
                        help="Plot and save graphs of the standardized data")
    parser.add_argument("-p", "--pca", action="store_true", dest="perform_pca",
                        help="Perform the PCA analysis and save related graphs")
    parser.add_argument("-c", "--cluster", action="store_true", dest="perform_clustering",
                        help="Perform the Clustering analysis and save related graphs")
    parser.add_argument("-n", "--num-dimensions", action="store", dest="num_dimensions", default=2, type=int,
                        help="Set the number of dimensions in the projected space (default: 2)")


    parser.add_argument("--style", action="store", dest="style", default="ggplot",
                        help="Set the matplotlib render style (default: ggplot)")
    parser.add_argument("--data", action="store", dest="data_filepath", default="./diabetes.csv",
                        help="Set the filepath of the data csv file. (default: ./diabetes.csv)")
    parser.add_argument("--out", action="store", dest="output_folderpath", default="graphs",
                        help="Set the output path of the folder to save graphs (default: graphs)")

    args = parser.parse_args()

    if(not(args.plot_raw_data) and not(args.plot_standardized_data) and
           not(args.perform_pca) and not(args.perform_lda)):
        parser.print_help()


    plt.style.use(args.style)

    df = data.read_data(args.data_filepath)

    if(args.plot_raw_data):
        plotting.plot_all_data(df, "Raw Data", os.path.join(args.output_folderpath, "raw"), data.column_names)

    if(args.plot_standardized_data):
        clean_df = data.clean_data(df)
        plotting.plot_all_data(clean_df, "Standardized Data", os.path.join(args.output_folderpath, "clean"), data.column_names)

    if(args.perform_pca):
        num_dimensions = args.num_dimensions
        projected_df = pca.perform_pca(df, num_dimensions)

        output_path = os.path.join(args.output_folderpath, "PCA")
        if(not(os.path.exists(output_path))):
            os.makedirs(output_path)

        plotting.plot_all_data(projected_df, "PCA {0}-D".format(num_dimensions), output_path, projected_df.columns)


    if(args.perform_clustering):
        print "Doing some Clustering stuff"
        print "Saving Clustering graphs"
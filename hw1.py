import pandas as pd
import ggplot as gg
import os

def create_graph(dataframe, x_col_index, y_col_index, column_names):
    x_column = column_names[x_col_index]
    y_column = column_names[y_col_index]
    color_column = column_names[0]
    return gg.ggplot(dataframe, gg.aes(x=x_column, y=y_column, color=color_column))

def save_graph(plt, title, filename):
    plt = plt + gg.geom_point() + \
          gg.scale_color_brewer(type="div", palette="RdBu") + \
          gg.ggtitle(title)
    plt.save(filename)


def clean_data(data_frame):
    result = data_frame.copy()
    result.x1 = result.x1 - data_frame.x1.mean()
    result.x2 = result.x2 - data_frame.x2.mean()

    result.x1 = result.x1 / data_frame.x1.std()
    result.x2 = result.x2 / data_frame.x2.std()


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


graph_num = 1
for x in range(1, len(column_names)-1):
    for y in range(1, len(column_names)):
        if x == y:
            continue
        plt = create_graph(df, x, y, column_names)
        save_graph(plt, "Raw Data", "./graphs/raw{0}.png".format(graph_num))
        graph_num += 1


#clean_df = clean_data(df)
#clean_plt = gg.ggplot(clean_df, gg.aes(x="Number of times pregnant", y="Plasma glucose concentration", color="Class Label"))
#save_graph(clean_plt, "Standardized Data", "./graphs/clean.png")
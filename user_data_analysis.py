"""
This module provides functions to be used in the command line interface (CLI) for user data analysis.
It includes functions to read data, solve specific questions, visualize data, create plots, and check for missing plots.
"""

import data_visualization
from pyspark_analyzer import *
from read_data import *
from data_visualization import *
from pathlib import Path
from dotenv import load_dotenv
import inspect
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from  configurations import *

load_dotenv()

DATA_PATH = Path(os.getenv("DATA_PATH"))
PLOT_PATH = Path(os.getenv("PLOT_PATH"))

def get_spark_session() -> SparkSession:
    """
    Create a Spark session
    :return: SparkSession
    """
    spark = create_spark_session()
    return spark

def get_parquet_data() -> pyspark.sql.DataFrame:
    """
    Get parquet data and return as a dataframe
    :return:  pyspark.sql.DataFrame
    """
    df = read_parquet_file(get_spark_session())
    return df

#Check this
def read_data(new_data: bool , data_min: float = 1 , verbose: bool= False) -> None:
    """
    Read data from API and save it in parquet format based on the click parameters
    :param new_data: bool
    :param data_min:
    :param verbose:
    :return:
    """

    data = get_data(read_new_data= new_data , get_data_min= data_min)
    if verbose:
        print("Information about data\n")
        print("Data shape : ", data.shape)
        print("Data columns : ", data.columns)
        print("Data types : ", data.dtypes)
        print("Data head : \n", data.head(2))



def solve_question(question_id: int , verbose: bool) -> None:
    """
    Solve specific questions based on the question ID
    :param question_id: int
    :param verbose: bool
    :return: None
    """
    spark = get_spark_session()
    df = get_parquet_data()
    create_temp_view(df)

    if question_id == 1:
        if verbose:
            print("Question 1")
        question_1_spark_sql(spark)
        question_1_dataframe_api(df)
    elif question_id == 2:
        if verbose:
            print("Question 2")
        question_2_spark_sql(spark)
        question_2_dataframe_api(df)
    elif question_id == 3:
        if verbose:
            print("Question 3")
        question_3_spark_sql(spark)
        question_3_dataframe_api(df)
    else:
        raise ValueError("Invalid question id")
    spark.stop()


def visualize_plot(path: str = PLOT_PATH) -> None:
    """
    Visualize the plots created in the specified path
    :param path: str
    :return: None
    """
    plot_list = os.listdir(f"{path}")
    print(plot_list)

    for plot in plot_list:
        if plot.endswith(".png"):
            print(f"Plot name : {plot}")
            plt_path = os.path.join(path, plot)
            img = mpimg.imread(plt_path)

            plt.figure(figsize=(12, 6))
            plt.imshow(img)
            plt.axis('off')  # Hide axis
            plt.title(plot)
            plt.tight_layout()
            plt.show()



def plot_creation(path:str = PLOT_PATH) -> None:
    """
    Create plots and save them to the specified path
    :param path: str
    :return: None
    """
    if not os.path.exists(path):
        os.makedirs(path)
    df = get_parquet_data()
    pd_df = df.toPandas()
    if check_plots(path):
        print("Plots already created. To see the plots, use the visualize command.")
    else:
        plot_gender_pie(pd_df,path)
        plot_usage_vs_avg(pd_df,path)
        plot_country_distribution_pie(pd_df,path)
        plot_age_distribution_bar(pd_df,path)
        plot_country_distribution_pie(pd_df,path)


def check_plots(path:str = PLOT_PATH) -> bool:
    """
    Check if the plots are created
    :param path: str
    :return: bool
    """
    plot_list = os.listdir(path)
    for plot in plot_list:
        if plot.endswith(".png"):
            return True
    return False


def get_plot_function_names () -> List[str]:
    """
    Get the names of all plot functions in the data_visualization module
    :return: List[str]
    """
    functions = inspect.getmembers(data_visualization, inspect.isfunction)
    plot_functions = [func_name for func_name, _ in functions if func_name.startswith("plot_")]
    return  plot_functions



def check_missing_plots( path: str = PLOT_PATH) -> None:
    """
    Check the plots that should have been created but missing
    :param path:
    :return:
    """
    func_names = get_plot_function_names()
    missing_plots = []
    existing_plots = [file.split('.')[0] for file in os.listdir(path) if file.endswith('.png')]

    for func in func_names:
        if func not in existing_plots:
            missing_plots.append(func)

    if missing_plots:
        print(f"Missing plots: {len(missing_plots)}")
        for missing in missing_plots:
            print(f"Plot '{missing}' has not been created.")
            create_specific_plot(missing,PLOT_PATH)
        print("To create the missing plots, run the create_plots command it will create missing plots.")
    else:
        print("All plots have been created.")


def create_specific_plot(function_name: str , path: str = PLOT_PATH) -> None:
    """
    Create a specific plot based on the function name
    :param function_name: str
    :param path: str
    :return: None
    """
    df = get_parquet_data()
    pd_df = df.toPandas()

    if hasattr(data_visualization,function_name):
        plot_func = getattr(data_visualization,function_name)
        plot_func(pd_df, path)
        print(f"Created plot {function_name}")
    else:
        print(f"Function {function_name} does not exist in data_visualization module.Try to run the "
              f"create_plots command to create all the plots , it should be create missing plots.")
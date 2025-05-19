from pyspark_analyzer import *
from read_data import *
from data_visualization import *

def read_data(new_data:bool,data_min:int,verbose:bool=False):
    data = get_data(read_new_data=new_data,get_data_min=data_min)
    if verbose:
        print("Information about data\n")
        print("Data shape : ", data.shape)
        print("Data columns : ", data.columns)
        print("Data types : ", data.dtypes)
        print("Data head : \n", data.head(2))

def solve_question(question_id:int,verbose:bool):

    print(f"solving question{question_id}")


# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# spark = create_spark_session()
# df = read_parquet_file(spark)
# df.printSchema()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("\n")
# """
# print("Plots about data")
# plot_gender_pie(df)
# plot_gender_hist_by_country(df)
# plot_age_distribution_bar(df)
# plot_usage_vs_avg(df)
# plot_country_distribution_pie(df)
#
# print("\n")
# """
# create_temp_view(df)
#
# question_1_spark_sql(spark)
# question_1_dataframe_api(df)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("\n")
# question_2_spark_sql(spark)
# question_2_dataframe_api(df)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("\n")
# question_3_spark_sql(spark)
# question_3_dataframe_api(df)
#
# spark.stop()
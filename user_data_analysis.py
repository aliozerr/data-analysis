from pyspark_analyzer import *
from read_data import *

data = get_data(False,1)
data.shape

print("\n")

spark = create_spark_session()

df = read_parquet_file(spark)
df.printSchema()

print("\n")

print("Sample data \n")
df.show(2)

print("\n")

create_temp_view(df)
question_1_spark_sql(spark)
print("\n")
question_1_dataframe_api(df)
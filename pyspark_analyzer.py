import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, floor, date_diff, current_timestamp, to_timestamp


def create_spark_session():
    """
    Create spark session
    """
    spark = SparkSession.builder.appName("UserDataAnalysis").getOrCreate()
    return spark


def calculate_age_and_usage_years(df:pyspark.sql.DataFrame) -> pyspark.sql.dataframe.DataFrame:
    """
    Take DataFrane formatted data for calculating age and usage_years
    :param df:pyspark.sql.DataFrame
    :return df:pyspark.sql.DataFrame
    """
    df = df.withColumn("age",floor(date_diff(current_timestamp(),to_timestamp("dob_date"))/365.25))
    df = df.withColumn("usage_years",floor(date_diff(current_timestamp(),to_timestamp("registered_date"))/365.25))
    return df

def create_temp_view(df:pyspark.sql.DataFrame):
    """
    Create temp. view called Users
    """
    df.createTempView("Users")


def read_parquet_file(spark) -> pyspark.sql.dataframe.DataFrame:
    """
    Read parquet format file , process it and return
    :param spark:
    :return df_processed:pyspark.sql.DataFrame
    """
    df = spark.read.parquet("user.parquet")
    df_processed = calculate_age_and_usage_years(df)
    return df_processed


def question_1_spark_sql(spark) -> pyspark.sql.dataframe.DataFrame:
    '''
    Erkek ve kadın kullanıcıların yaş ortalamasını bulun. Ayrıca, sosyal medya uygulamasını
    ortalama ne kadar süredir kullandıklarını bulun.
    '''
    print("Question 1 , Spark SQL Solution :\n")
    result = spark.sql(
        """
        SELECT u.gender , ROUND(AVG(u.age),4) AS avg_age , ROUND(AVG(u.usage_years),4) AS avg_usage_years
        FROM Users u
        GROUP BY u.gender
        """
    )
    result.show()
    return result

def question_1_dataframe_api(df) -> pyspark.sql.dataframe.DataFrame:
    """
    Erkek ve kadın kullanıcıların yaş ortalamasını bulun. Ayrıca, sosyal medya uygulamasını
    ortalama ne kadar süredir kullandıklarını bulun.
    """
    print("Question 1, DataframeAPI Solution : \n")
    result = df.groupBy("gender") \
                .agg(round(avg("age"),4).alias("avg_age"),round(avg("usage_years"),4).alias("avg_usage_years")) \
                .orderBy("gender")
    result.show()
    return result



def question_2_spark_sql(spark)-> pyspark.sql.dataframe.DataFrame:
    '''
    Ülkelere göre erkek ve kadın kullanıcıların yaş ortalamasını bulun. Ayrıca, sosyal medya
    uygulamasını ortalama ne kadar süredir kullandıklarını bulun.
    '''
    print("Question 2 , Spark SQL Solution :\n")
    result = spark.sql(
        """
        SELECT 
            u.location_country AS country , 
            u.gender , ROUND(AVG(u.age),4) AS avg_age , 
            ROUND(AVG(u.usage_years),4) AS avg_usage_years
        FROM Users u
        GROUP BY u.location_country, u.gender
        ORDER BY u.location_country, u.gender
        """
    )
    result.show()
    return result

def question_2_dataframe_api(df)-> pyspark.sql.dataframe.DataFrame:
    """
    Ülkelere göre erkek ve kadın kullanıcıların yaş ortalamasını bulun. Ayrıca, sosyal medya
    uygulamasını ortalama ne kadar süredir kullandıklarını bulun.
    """
    print("Question 2,DataframeAPI Solution : \n")
    result = df.groupBy("location_country","gender") \
                .agg(round(avg("age"),4).alias("avg_age"),round(avg("usage_years"),4).alias("avg_usage_years")) \
                .orderBy("location_country","gender")
    result.show()
    return result


def question_3_spark_sql(spark) -> pyspark.sql.dataframe.DataFrame:
    '''
    Ülkelere göre en yaşlı 3 erkek ve kadın kullanıcıyı bulun.
    '''
    print("Question 3 , Spark SQL Solution : \n")
    result = spark.sql(
        """
        SELECT *
        FROM (
            SELECT
                CONCAT(u.name_first, " ", u.name_last) as full_name,
                u.age,
                u.gender,
                u.location_country,
                RANK() OVER (PARTITION BY location_country, gender ORDER BY age DESC) AS rank
            FROM Users u
            WHERE u.gender = "male"
        ) RankedMaleUsers
        WHERE RankedMaleUsers.rank <= 3

        UNION ALL

        SELECT *
        FROM (
            SELECT
                CONCAT(u.name_first, " ", u.name_last) as full_name,
                u.age,
                u.gender,
                u.location_country,
                RANK() OVER (PARTITION BY location_country, gender ORDER BY age DESC) AS rank
            FROM Users u
            WHERE u.gender = "female"
        ) RankedFemaleUsers
        WHERE RankedFemaleUsers.rank <= 3

        ORDER BY location_country, gender, rank
        """
    )
    result.show(50)
    return result


def question_3_dataframe_api(df) -> pyspark.sql.dataframe.DataFrame:
    '''
    Ülkelere göre en yaşlı 3 erkek ve kadın kullanıcıyı bulun.
    '''
    print("Question 3 , Dataframe API Solution : \n")

    full_name_df = df.withColumn("full_name", concat_ws(" ", col("name_first"), col("name_last")))

    male_df = full_name_df.filter(col("gender") == "male")
    female_df = full_name_df.filter(col("gender") == "female")

    window_func = Window.partitionBy("location_country", "gender").orderBy(col("age").desc())

    ranked_male_df = male_df.withColumn("rank", rank().over(window_func))
    ranked_female_df = female_df.withColumn("rank", rank().over(window_func))

    top_3_male = ranked_male_df.filter(col("rank") <= 3)
    top_3_female = ranked_female_df.filter(col("rank") <= 3)

    result = top_3_male.unionByName(top_3_female)
    result = result.select("full_name", "age", "gender", "location_country", "rank").orderBy("location_country",
                                                                                             "gender", "rank")
    result.show(50)
    return result

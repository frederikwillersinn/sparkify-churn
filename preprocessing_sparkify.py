from datetime import datetime
import pyspark.sql.functions as F
from pyspark.sql.functions import udf 
from pyspark.sql.types import StringType


def get_value_counts(df, column, n=20):
    """Returns the n top value counts of a Pyspark dataframe column."""
    return df.groupBy(column).count().orderBy("count", ascending=False).show(n, truncate=False)


def get_nunique(df, column):
    """Returns the number of unique values in a Pyspark dataframe column."""
    return df.groupBy(column).count().sort("count").count()


def get_unique(df, column, n=20):
    """Returns the sorted top n unique values in a Pyspark dataframe column."""
    return df.select(column).dropDuplicates().orderBy(column).show(n, truncate=False)


def dropna(df, column):
    """Removes missing and invalid records from a Pyspark dataframe."""
    df = df.filter((df[column].cast(StringType()) != "") & (df[column].isNotNull()))
    return df


def timestamp_to_date(df, column):
    """Assigns a new column 'date' from a timestamp column."""
    to_date = udf(lambda x: datetime.fromtimestamp(x / 1000).strftime("%Y-%m-%d"))
    df = df.withColumn("date", to_date(df[column]))
    return df


def timestamp_to_weekday(df, column):
    """Assigns a new column 'weekday' from a timestamp column."""
    to_date = udf(lambda x: datetime.fromtimestamp(x / 1000).strftime("%A"))
    df = df.withColumn("weekday", to_date(df[column]))
    return df

def preprocess_sparkify_data(df):
    """Preprocesses the sparkify dataframe for predicting churn."""
    df = dropna(df, "userId")
    df = dropna(df, "sessionId")
    df = df.withColumn("churn", F.when(df["page"] == "Cancellation Confirmation", 1).otherwise(0))
    df = timestamp_to_date(df, column="ts")
    df = timestamp_to_weekday(df, column="ts")
    return df

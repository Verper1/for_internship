import pytest
import os
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = r"C:\Users\skuf\PycharmProjects\for_internship\.venv\Scripts\python.exe"

@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder \
        .appName("pytest-pyspark") \
        .master("local[*]") \
        .getOrCreate()
    yield spark
    spark.stop()

# Databricks notebook source
spark.conf.set(
  "fs.azure.account.key.storagedatalakejas.dfs.core.windows.net",
  "<paste your token>"
)

# Read the csv file

df = spark.read.format("csv") \
    .option("header", "true") \
    .load("abfss://silver@storagedatalakejas.dfs.core.windows.net/sales_data_clean.csv")

df.display()

# print schema

df.printSchema()

# Convert the data types

from pyspark.sql.functions import col

df_clean = df.withColumn("Quantity", col("Quantity").cast("int")) \
             .withColumn("UnitPrice", col("UnitPrice").cast("double"))

# check for new datatypes

df_clean.printSchema()

# Remove null values

df_clean = df_clean.dropna()

# Remove Duplicates

df_clean = df_clean.dropDuplicates()

# Adding a new column total_sales

from pyspark.sql.functions import expr

df_clean = df_clean.withColumn("Total_Sales", expr("Quantity * UnitPrice"))
df_clean.display()

# loading the file to GOLD

df_clean.write.mode("overwrite") \
    .format("csv") \
    .option("header", "true") \
    .save("abfss://gold@storagedatalakejas.dfs.core.windows.net/sales_gold")




# Databricks notebook source
# DBTITLE 1,Import the required library
import requests
import json
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# DBTITLE 1,Create Catalog, Schema and Volume
spark.sql("CREATE CATALOG IF NOT EXISTS workspace")
spark.sql("CREATE SCHEMA IF NOT EXISTS workspace.default")
spark.sql("CREATE VOLUME IF NOT EXISTS workspace.default.cricket_api_project")
base_path = '/Volumes/workspace/default/cricket_api_project'



# COMMAND ----------

# DBTITLE 1,Caling Cricket API
API_KEY='dd4dd816-1fa4-4d7b-9476-06a18b611072'

api_url=f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0"

response = requests.get(api_url)
response.raise_for_status() 
# if any error/issue comes it will raise issue change in api key to see(Exception handling)

api_data = response.json()
print(api_data.keys())

print(json.dumps(api_data, indent=2)[:2000])

# COMMAND ----------

# DBTITLE 1,Save Raw API Response in Volume
raw_file_path = f'{base_path}/current_matches_raw.json'

with open (raw_file_path, 'w') as file:
    json.dump(api_data,file)
# print("RAW API data is save at :",raw_file_path)


# COMMAND ----------

# DBTITLE 1,Create Bronze Layer Dataframe or Table
bronze_data = [{
    "source_api" : api_url,
    "raw_json" : json.dumps(api_data),
    "ingestion_time" : None
}]
#bronze_data (printing data)

bronze_schema = StructType([
    StructField("source_api", StringType(),True),
    StructField("raw_json", StringType(),True),
    StructField("ingestion_time", TimestampType(), True)
])
#bronze_schema (printing schema)

bronze_df = spark.createDataFrame(bronze_data, bronze_schema) \
    .withColumn("ingestion_time", current_timestamp())

display(bronze_df)

# COMMAND ----------

# DBTITLE 1,Save The Bronze Table
bronze_df.write\
    .format('delta')\
    .mode('overwrite')\
    .saveAsTable("workspace.default.cricket_bronze_current_matches")
#we are creating managed table in unity catalog name is workspace, table name is cricket..., schema name is default

print("BRONZE TABLE CREATED SUCCESSFULLY")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from workspace.default.cricket_bronze_current_matches

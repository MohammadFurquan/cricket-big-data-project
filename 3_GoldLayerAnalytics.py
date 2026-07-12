# Databricks notebook source
# DBTITLE 1,Importing Libraries
from pyspark.sql.functions import *

# COMMAND ----------

# DBTITLE 1,Read the silver layer
silver_df = spark.table('workspace.default.cricket_silver_current_matches')
display(silver_df)

# COMMAND ----------

# DBTITLE 1,Gold Analytics 1 : Match type distribution
gold_match_type_df = silver_df.groupBy('match_type').agg(count('*').alias('Total_Matches'))
display(gold_match_type_df)

# COMMAND ----------

# DBTITLE 1,Gold Analytics 2 : Venue-Wise Match Count
gold_venue_df = silver_df.groupBy('venue').agg(count('*').alias('Total_Matches'))

display(gold_venue_df)

# COMMAND ----------

# DBTITLE 1,Gold Analytics 3 : Team Wise Match Count
team1_df = silver_df.select(col("team_1").alias("team"))
team2_df = silver_df.select(col("team_2").alias("team"))
all_team_df = team1_df.union(team2_df)
gold_team_df = all_team_df.groupBy('team')\
    .agg(count('*').alias("matches_played"))


display(gold_team_df)                             

# COMMAND ----------

# DBTITLE 1,Final Analytics Queries
# Match Overview
display(spark.sql("""select count(*) as Total_matches,
count(distinct match_type) AS total_match_types,
count(distinct venue) AS Total_venues
FROM workspace.default.cricket_silver_current_matches"""))

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) as Total_matches,
# MAGIC count(distinct match_type) AS total_match_types,
# MAGIC count(distinct venue) AS Total_venues
# MAGIC FROM workspace.default.cricket_silver_current_matches
# MAGIC

# COMMAND ----------



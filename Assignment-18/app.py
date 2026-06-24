from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("PartitionManagement") \
    .getOrCreate()

# Generate DataFrame with 5 million records
df = spark.range(0, 5000000)

# Display initial number of partitions
initial_partitions = df.rdd.getNumPartitions()
print(f"Initial Number of Partitions: {initial_partitions}")

# Increase partitions to 12
df_repartitioned = df.repartition(12)
repartitioned_partitions = df_repartitioned.rdd.getNumPartitions()
print(f"Number of Partitions after Repartition(12): {repartitioned_partitions}")

# Reduce partitions to 3
df_coalesced = df_repartitioned.coalesce(3)
coalesced_partitions = df_coalesced.rdd.getNumPartitions()
print(f"Number of Partitions after Coalesce(3): {coalesced_partitions}")

# Display sample records
print("Sample Records:")
df_coalesced.show(10)

# Stop Spark Session
spark.stop()
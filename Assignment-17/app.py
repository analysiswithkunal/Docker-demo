from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("SalesAnalysis") \
    .getOrCreate()

# Read CSV File
df = spark.read.csv(
    "sales_data.csv",
    header=True,
    inferSchema=True
)

print("\n===== Original Dataset =====")
df.show()

# Sort products by sales descending
print("\n===== Products Sorted by Sales (Descending) =====")
sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

# Top 3 highest sales products
print("\n===== Top 3 Products by Sales =====")
top3_df = sorted_df.limit(3)
top3_df.show()

# Filter products with sales > 80000
print("\n===== Products with Sales > 80000 =====")
high_sales_df = df.filter(col("sales") > 80000)
high_sales_df.show()

# Save filtered output as CSV
high_sales_df.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output/high_sales_products")

print("\nFiltered data saved successfully.")

spark.stop()
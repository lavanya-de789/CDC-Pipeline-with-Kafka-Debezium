from pyspark.sql import SparkSession

spark=(SparkSession.builder
.appName('SilverLayer')
.getOrCreate())

bronze=spark.read.parquet(
'data/bronze'
)

clean=bronze.dropDuplicates()

clean.write.mode(
'overwrite'
).parquet(
'data/silver'
)

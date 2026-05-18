from pyspark.sql import SparkSession

spark=(SparkSession.builder
.appName('CDCConsumer')
.getOrCreate())

raw=(spark.readStream
.format('kafka')
.option(
'kafka.bootstrap.servers',
'localhost:9092'
)
.option(
'subscribe',
'postgres.public.customers'
)
.load())

parsed=raw.selectExpr(
'CAST(value AS STRING)'
)

query=(parsed.writeStream
.format('parquet')
.option(
'path',
'data/bronze'
)
.option(
'checkpointLocation',
'data/checkpoint'
)
.start())

query.awaitTermination()

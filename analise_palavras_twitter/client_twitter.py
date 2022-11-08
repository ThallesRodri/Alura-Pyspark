from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()

lines = spark.readStream\
    .format('socket')\
    .option('host','localhost')\
    .option('port',9009)\
    .load()

words = lines.select(F.explode(F.split(lines.value, ' ')).alias('word'))

wordsCounts = words.groupBy('word').count()

query = wordsCounts.writeStream\
    .outputMode('complete')\
    .format('console')\
    .start()

query.awaitTermination()
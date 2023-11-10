from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp
spark = SparkSession.builder.appName('dataProcessing').getOrCreate()

df = spark.read.csv('spotify.csv', header=True)

df.show()
df.printSchema()


#transforming the year variable from string to timestamp
df = df.withColumn('year', to_timestamp(col('year'), 'yyyy'))

print ('After transforming the year variable from string to timestamp')

df.printSchema()


#top 10 songs with danceability
df = df.filter(col('danceability') <= 1) #removing an erroneous value
top10 = df.orderBy(col('danceability').desc())\
           .select('track_name', 'artist_name', 'danceability').limit(10)

top10.write.mode('overwrite').csv('top10.csv')
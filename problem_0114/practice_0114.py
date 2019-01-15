from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CSVExercise").getOrCreate()

csvDF = spark.read.option("header", "true").option("inferSchema", "true").csv("name.csv")
print(csvDF.printSchema())
print(csvDF.show())

csvDF.write.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.output.uri","mongodb://localhost:27017/exercise.csv").save()
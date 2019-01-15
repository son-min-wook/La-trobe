from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("CSVExercise").getOrCreate()
df = spark.read.option("header","true").option("inferSchema","true").csv("name.csv")
df1 = spark.read.option("header","true").option("inferSchema","true").csv("address.csv")
df2=df.join(df1,'name')
df2.filter("age <25").show()
#df2.write.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.output.uri","mongodb://localhost:27017/join.csv").save()
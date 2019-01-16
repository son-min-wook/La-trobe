from pyspark.sql import SparkSession as ss
import pandas as pd
import numpy as np
from pyspark.sql import SQLContext
from pyspark import SparkConf, SparkContext
sc = SparkContext(master="local",appName="Spark Demo")
sqlContext = SQLContext(sc)
spark = ss.builder.getOrCreate()
df1 = spark.read.csv("1.csv", inferSchema = True)
df2 = spark.read.csv("2.csv", inferSchema = True)
df3 = df1.toPandas()
df4 = df2.toPandas()
list = np.array(df3).tolist()
list1 = np.array(df4).tolist()
i=1
list3=[]
len1 =len(list)
len2 = len(list1)
if len1 <= len2:
    len1=len1
else:
    len1=len2
for value in range(len1-1):
    list3.append(int(list[i][0])+int(list1[i][0]))
    i=i+1
df = pd.DataFrame(list3)
print (df)
result =spark.createDataFrame(df,["result"])
result.show()
#result.write.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.output.uri","mongodb://localhost:27017/problem_0116.csv").save()




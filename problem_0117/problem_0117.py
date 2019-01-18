from pyspark.sql import SparkSession as ss
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from matplotlib.image import imread
from pylab import figure, axes, pie, title, show
spark = ss.builder.getOrCreate()
df1 = spark.read.option("header", "true").csv("age.csv", inferSchema = True)
df2 = spark.read.option("header", "true").csv("grade.csv", inferSchema = True)

# spark -> pandas
df3 = df1.toPandas()
df4 = df2.toPandas()

#pandas -> list
list = np.array(df3).tolist()
list1 = np.array(df4).tolist()

y=[]
x=[]
q=[]
w=[]
i=0
for value in range(len(list)):
    x.append(list[i][0])
    y.append(list[i][1])
    i+=1
i=0
for value in range(len(list1)):
    q.append(list1[i][0])
    w.append(list1[i][1])
    i+=1

n_group=len(x)
n_group1=len(q)
index=np.arange(n_group)
index1=np.arange(n_group1)
plt.bar(index,y,tick_label = x,align='center')
plt.xlabel('name')
plt.ylabel('age')
plt.savefig('result1.png')
plt.show()

plt2.plot(q,w,marker="o")
plt2.xlabel('name')
plt2.ylabel('grade')
plt2.savefig('result2.png')
plt2.show()





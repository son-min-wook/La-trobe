import json
import matplotlib.pyplot as plt
import numpy as np
with open('problem3.json') as data_file:
    data = json.load(data_file)
print('Welcome to Birth.Dictionary')
i = 0
count = 0
month = ["January","February","March","April","May","June","July","August","September",
         "October","November","December" ]
mon = ["/01/","/02/","/03","/04","/05/","/06/","/07/","/08/","/09/","/10/","/11/","/12/"]
result=[None] * 12
for i in range(0,12):
   for value in  data:
      if data[value].find(mon[i])>0:
          count +=1
   print (month[i],"has",count,"friends")
   result[i]= count
   i = i + 1
   count = 0
v1_value = result
x_name = month
n_group = len(x_name)
index = np.arange(n_group)

plt.bar(index,v1_value,tick_label = x_name,align='center')

plt.xlabel('month')
plt.ylabel('people')
plt.title('Birthday month')
plt.xlim(-1,n_group)
plt.ylim(0, 7)
plt.show()

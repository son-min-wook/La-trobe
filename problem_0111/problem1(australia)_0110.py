import matplotlib.pyplot as plt
import numpy as np
import csv
f=open('australia.csv','r',encoding='UTF-8-sig')
lines =csv.reader(f)
a_name=[]
a_Sub_saharan_africa =[]
a_South_asia=[]
a_middle_east=[]
a_latin_america=[]
a_europe=[]
a_east_asia=[]
a_high=[]
a_residual=[]
j = 0
for data_s in lines:
    a_name.append(data_s[0])
    if j==0:
        for k in range(0,7):
          a_Sub_saharan_africa.append(data_s[k+1])
          k=k+1
    elif j==1:
        for k in range(0, 7):
          a_South_asia.append(data_s[k+1])
          k = k + 1
    elif j==2:
        for k in range(0, 7):
          a_middle_east.append(data_s[k+1])
          k = k + 1
    elif j==3:
        for k in range(0, 7):
          a_latin_america.append(data_s[k+1])
          k = k + 1
    elif j==4:
        for k in range(0, 7):
          a_europe.append(data_s[k+1])
          k = k + 1
    elif j==5:
        for k in range(0, 7):
          a_east_asia.append(data_s[k+1])
          k = k + 1
    elif j==6:
        for k in range(0, 7):
          a_high.append(data_s[k+1])

          k = k + 1
    elif j==7:
        for k in range(0, 7):
          a_residual.append(data_s[k+1])
          k = k + 1
    k=0
    j=j+1
f.close()

for i in range(0,7):
 colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red','m','b','c']
 labels = [a_name[0],a_name[1],a_name[2],a_name[3],a_name[4],a_name[5],a_name[6],a_name[7]]
 ratio = [a_Sub_saharan_africa[i], a_South_asia[i], a_middle_east[i], a_latin_america[i], a_europe[i],a_east_asia[i],a_high[i], a_residual[i]]
 plt.pie(ratio,  labels=labels,colors=colors, autopct='%2.5f%%', startangle=180)
 plt.title('Merchandise exports to low- and middle-income economies  (% of total merchandise exports)- Australia')
 plt.show()

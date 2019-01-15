import matplotlib.pyplot as plt
import numpy as np
import csv
f=open('korea.csv','r',encoding='UTF-8-sig')
lines =csv.reader(f)
k_name=[]
k_year=['1981~1985','1986~1990','1991~1995','1996~2000','2001~2005','2006~2010','2010~2016']
k_Sub_saharan_africa =[]
k_South_asia=[]
k_middle_east=[]
k_latin_america=[]
k_europe=[]
k_east_asia=[]
k_high=[]
k_residual=[]
j = 0
for data_s in lines:
    k_name.append(data_s[0])
    if j == 0:
        for k in range(0, 7):
            k_Sub_saharan_africa.append(data_s[k + 1])
            k = k + 1
    elif j == 1:
        for k in range(0, 7):
            k_South_asia.append(data_s[k + 1])
            k = k + 1
    elif j == 2:
        for k in range(0, 7):
            k_middle_east.append(data_s[k + 1])
            k = k + 1
    elif j == 3:
        for k in range(0, 7):
            k_latin_america.append(data_s[k + 1])
            k = k + 1
    elif j == 4:
        for k in range(0, 7):
            k_europe.append(data_s[k + 1])
            k = k + 1
    elif j == 5:
        for k in range(0, 7):
            k_east_asia.append(data_s[k + 1])
            k = k + 1
    elif j == 6:
        for k in range(0, 7):
            k_high.append(data_s[k + 1])
            k = k + 1
    elif j == 7:
        for k in range(0, 7):
            k_residual.append(data_s[k + 1])
            k = k + 1
    k = 0
    j = j + 1
f.close()
while True:
    print('------------------')
    print('Press the number that you want to do')
    print('1. Pie chart for all years')
    print('2. Line graph for each merchandise')
    print('3. Exit')
    select = int(input('What work do you want to?:'))
    if select  == 1:
        q=0
        for i in range(0,7):
         colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red','m','b','c']
         labels = [k_name[0],k_name[1],k_name[2],k_name[3],k_name[4],k_name[5],k_name[6],k_name[7]]
         ratio = [k_Sub_saharan_africa[i], k_South_asia[i], k_middle_east[i], k_latin_america[i], k_europe[i],k_east_asia[i],k_high[i], k_residual[i]]
         plt.pie(ratio,  labels=labels,colors=colors, autopct='%2.5f%%', startangle=180)
         plt.title('Merchandise exports to low- and middle-income economies  (% of total merchandise exports) - Korea '+k_year[q])
         q=q+1
         plt.show()
    elif select == 2:
        plt.plot([1, 2, 3, 4])
        plt.xlabel('% of total merchandise exports')
        plt.ylabel('y-axis')
        plt.show()
    elif select == 3:
        break
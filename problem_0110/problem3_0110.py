import json
with open('problem3.json') as data_file:
    data = json.load(data_file)
print('Welcome to Birth.Dictionary')
i = 0
count = 0
month = ["January","February","March","April","May","June","July","August","September",
         "October","November","December" ]
mon = ["/01/","/02/","/03","/04","/05/","/06/","/07/","/08/","/09/","/10/","/11/","/12/"]
for i in range(0,12):
   for value in  data:
      if data[value].find(mon[i])>0:
          count +=1
   print (month[i],"has",count,"friends")
   i = i + 1
   count = 0
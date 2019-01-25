from pymongo import MongoClient
import requests
import time

latrobe_bundoora='http://api.openweathermap.org/data/2.5/weather?zip=3086,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'
monash_clayton='http://api.openweathermap.org/data/2.5/weather?zip=3800,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'
monash_caulfield='http://api.openweathermap.org/data/2.5/weather?zip=3145,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'
res_bundoora = requests.get(latrobe_bundoora)
res_clayton = requests.get(monash_clayton)
res_caulfield = requests.get(monash_caulfield)
data_bundoora =res_bundoora.json()
data_clayton = res_clayton.json()
data_caulfield = res_caulfield.json()
temperature_bundoora = data_bundoora['main']['temp']
temperature_clayton = data_clayton['main']['temp']
temperature_caulfield = data_caulfield['main']['temp']

print('Temparature of Bundoora Campus==' + str(temperature_bundoora))
print('Temparature of Clayton Campus==' + str(temperature_clayton))
print('Temparature of Caulfield Campus==' + str(temperature_caulfield))
col = ["bundoora", "clayton", "caulfield"]
now = time.localtime()
s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
tempera=[[float(temperature_bundoora),'0'],[float(temperature_clayton),'1'],[float(temperature_caulfield),'2']]
min_v = 9999
max_v = -999
i=0
min_num=-1
max_num=-1
for x in range(0,3):
    if float(tempera[i][0]) < min_v:
        min_v=tempera[i][0]
        min_num=i
    if float(tempera[i][0]) > max_v:
        max_v=tempera[i][0]
        max_num=i
    i=i+1
print(s,"'s hottest place: ",col[int(tempera[max_num][1])])
print(s,"'s collest place: ",col[int(tempera[min_num][1])])

client = MongoClient('localhost', 27017)
db = client['temperature']
collection = db['3school']
quert=[{"name": "bundoora"},{"name":"clayton"},{"name":"caulfield"}]
av=[0,0,0]
for t in range(0,3):
    count = 0
    i = 0
    for x in collection.find(quert[t]).sort("main.temp",-1):
        x=collection.find(quert[t]).sort("main.temp", -1)[i]["main"]["temp"]
        av[t]=av[t]+x
        count=count+1
        i=i+1
    av[t]=av[t]/count
    print(col[t],"'s avg: ",av[t])






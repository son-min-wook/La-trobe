import requests
import time
from pymongo import MongoClient
latrobe_bundoora='http://api.openweathermap.org/data/2.5/weather?zip=3086,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'
monash_clayton='http://api.openweathermap.org/data/2.5/weather?zip=3800,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'
monash_caulfield='http://api.openweathermap.org/data/2.5/weather?zip=3145,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'


#make a request to the collect the dat
res_bundoora = requests.get(latrobe_bundoora)
res_clayton = requests.get(monash_clayton)
res_caulfield = requests.get(monash_caulfield)

#get data as json format
data_bundoora =res_bundoora.json()
data_clayton = res_clayton.json()
data_caulfield = res_caulfield.json()

#collect the temperature data
temperature_bundoora = data_bundoora['main']['temp']
temperature_clayton = data_clayton['main']['temp']
temperature_caulfield = data_caulfield['main']['temp']


# printing the temperature data in every 10 minutes 5 second.
#The website publishes new data in every 10 minutes
while True:
    print('Temparature of Bundoora Campus==' + str(temperature_bundoora))
    print('Temparature of Clayton Campus==' + str(temperature_clayton))
    print('Temparature of Caulfield Campus==' + str(temperature_caulfield))
    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    print(s)
    rj = res_bundoora.json()
    clj = res_clayton.json()
    caj = res_caulfield.json()
    rj['time'] = s
    clj['time'] = s
    caj['time'] = s
    rj['name'] = 'bundoora'
    clj['name'] = 'clayton'
    caj['name'] = 'caulfield'

    # Create connection to MongoDB
    client = MongoClient('localhost', 27017)
    db = client['temperature']
    collection = db['3school']

    # Insert the dictionary into Mongo
    collection.insert_one(rj)
    collection.insert_one(clj)
    collection.insert_one(caj)
    time.sleep(605)
    print('New set:')


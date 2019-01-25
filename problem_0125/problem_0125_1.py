import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
import requests
from pylab import legend
from pymongo import MongoClient

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,1,1)
ax3 = fig.add_subplot(1,1,1)
xar = []
yar = []
bunar=[]
caular=[]
clayar=[]


times=[]
def animate(i):
    latrobe_bundoora = 'http://api.openweathermap.org/data/2.5/weather?zip=3086,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'
    monash_clayton = 'http://api.openweathermap.org/data/2.5/weather?zip=3800,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'
    monash_caulfield = 'http://api.openweathermap.org/data/2.5/weather?zip=3145,au&units=metric&APPID=d69a4b6015c26ca2ef20c16aecdeaee8'

    # make a request to the collect the dat
    res_bundoora = requests.get(latrobe_bundoora)
    res_clayton = requests.get(monash_clayton)
    res_caulfield = requests.get(monash_caulfield)

    # get data as json format
    data_bundoora = res_bundoora.json()
    data_clayton = res_clayton.json()
    data_caulfield = res_caulfield.json()

    # collect the temperature data
    temperature_bundoora = data_bundoora['main']['temp']
    temperature_clayton = data_clayton['main']['temp']
    temperature_caulfield = data_caulfield['main']['temp']
    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    print(s)
    times.append(s)

    bun,clay,caul,y = temperature_bundoora,temperature_clayton,temperature_caulfield,s

    print("bun: ",bun)
    print("clay: ",clay)
    print("caul: ",caul)
    print(y)
    print("---")
    bunar.append(bun)
    clayar.append(clay)
    caular.append(caul)
    yar.append(y)
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax1.plot(yar,bunar)
    ax2.plot(yar,clayar)
    ax3.plot(yar,caular)
    plt.xlabel("time")
    plt.ylabel("temperature")
    plt.legend(['bundoora','clayton','caulfield'])




ani = animation.FuncAnimation(fig, animate, interval=605000)
plt.show()

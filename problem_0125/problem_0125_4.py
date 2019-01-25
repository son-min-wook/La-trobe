import requests
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
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
    col=["bundoora","clayton","caulfield"]
    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    print(s)
    times=[s]
    tempera=np.array([[float(temperature_bundoora),float(temperature_clayton),float(temperature_caulfield)]])
    fig, ax = plt.subplots()
    im = ax.imshow(tempera)
    ax.set_xticks(np.arange(len(col)))
    ax.set_yticks(np.arange(len(times)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(col)
    ax.set_yticklabels(times)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(times)):
        for j in range(len(col)):
            text = ax.text(j, i, tempera[i, j],
                           ha="center", va="center", color="w")

    ax.set_title("Temperature for each school")
    fig.tight_layout()
    plt.show()
    time.sleep(605)
    print('New set:')


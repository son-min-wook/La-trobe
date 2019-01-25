from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['temperature']
collection = db['3school']

bunquery={"name":"bundoora"}
clayquery={"name":"clayton"}
calquery={"name":"caulfield"}

bunmax = collection.find(bunquery).sort("main.temp",-1)[0]["main"]["temp"]
claymax = collection.find(clayquery).sort("main.temp",-1)[0]["main"]["temp"]
calmax = collection.find(calquery).sort("main.temp",-1)[0]["main"]["temp"]

bunmax_t = collection.find(bunquery).sort("main.temp",-1)[0]["time"]
claymax_t = collection.find(clayquery).sort("main.temp",-1)[0]["time"]
calmax_t = collection.find(calquery).sort("main.temp",-1)[0]["time"]

print("Bundoora")
print("Max: ",bunmax)
print("Max_time: ",bunmax_t)
print("Clayton")
print("Max: ",claymax)
print("Max_time: ",claymax_t)
print("Caulfield")
print("Max: ",calmax)
print("Max_time: ",calmax_t)


bunmin = collection.find(bunquery).sort("main.temp",1)[0]["main"]["temp"]
claymin = collection.find(clayquery).sort("main.temp",1)[0]["main"]["temp"]
calmin = collection.find(calquery).sort("main.temp",1)[0]["main"]["temp"]

bunmin_t = collection.find(bunquery).sort("main.temp",1)[0]["time"]
claymin_t = collection.find(clayquery).sort("main.temp",1)[0]["time"]
calmin_t = collection.find(calquery).sort("main.temp",1)[0]["time"]

print("Bundoora")
print("Min: ",bunmin)
print("Min_time: ",bunmin_t)
print("Clayton")
print("Min: ",claymin)
print("Min_time: ",claymin_t)
print("Caulfield")
print("Min: ",calmin)
print("Min_time: ",calmin_t)

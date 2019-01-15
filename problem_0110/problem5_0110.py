import json
with open('problem3.json') as data_file:
    data = json.load(data_file)
print('Welcome to Birth.Dictionary')
i = 0
people =0
totalage =0
for value in data:
  people += 1
age=[]
for value in data:
  age.append(2019-int(data[value][6:]))
  i+=1

for t in range(people):
    totalage +=age[t]
    i+=1

age.sort()
print ("average of age: ",totalage/people)
print ("mean of age: ",age[people//2])

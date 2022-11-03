# Find Mode 

def freq(list,item):
    f = list.count(item)     
    return f

def modeSoFar(list):
  
  modeSoFar = list[0]
  freqSoFar = freq(list,modeSoFar)  

  for item in list[1:]:
    if freq(list,item)> freqSoFar:
      modeSoFar = item
      freqSoFar = freq(list,item)
  return modeSoFar


list = [1,2,4,4,6,1,2,3,4,2,4,1,4,2,2,2]
print("Mode of list -->", modeSoFar(list))


# Find Mode Fast
import random

def buildRandomList(size,maxvalue):
    result = [random.randrange(maxvalue) for x in range(size)]
    return result 

dataset = buildRandomList(100,100)

def fastMode(dataset):
    tallies = [0]*100
    for item in dataset:
        tallies[item]+=1 
    highest = max(tallies)
    value = tallies.index(highest)
    return value 

result = fastMode(dataset)
print("Fast Mode -->", result)




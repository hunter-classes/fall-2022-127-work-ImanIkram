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








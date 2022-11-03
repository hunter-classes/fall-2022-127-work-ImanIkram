'''findLargest(l) which takes in a list of numbers and returns the value of the smallest number
freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the freuqeency
of v, that is, the number of times that v appears in l.
'''

#Find frequency 
def freq(l,v):
    f = l.count(v)     
    return f

num = [1,2,3,4,8,3,2,8,4,0,3,2,3]
print ("frequency -->", freq(num,3))

#Find Largest 
def findLargest(l):
    large = 0
    for n in l:
        if large < n:
          large = n
    return large

l2 = [13,34,65,34,67,9,54,32,12,11,10]
print ("Largest value -->", findLargest(l2))


#Find Mode Fast
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






     
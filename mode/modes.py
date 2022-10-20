'''findLargest(l) which takes in a list of numbers and returns the value of the smallest number
freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the freuqeency
of v, that is, the number of times that v appears in l.
'''

def findSmallest(s):
  small = min(s)
  return small

l1 = [13,34,65,34,67,9,54,32,12,11,10]
print ("minimum value in l1 -->", findSmallest(l1))


def freq(l,v):
    f = l.count(v)     
    return f

num = [1,2,3,4,8,3,2,8,4,0,3,2,3]
print ("frequency -->", freq(num,3))






     
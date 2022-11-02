# 5, 7, 8

# 5 Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)

def max(lst):
    num = 0
    for n in lst:
        if num < n:
            num = n
    return num
     
grades = [99,87,67,78,89,100,57]
print(max(grades))


# 7 Write a function to count how many odd numbers are in a list.
def countOdd(lst):
    odd = 0
    for n in lst:
        if n % 2 != 0:
            odd = odd + 1
    return odd
            
            
l1 = [6,4,3,5,9,11,56,89,99]
print(countOdd(l1))

# 8 Sum up all the even numbers in a list.

def sumEven(lst):
    even = 0
    for n in lst:
        if n % 2 == 0:
            even = even + n
    return even
            
          
l1 = [6,5,2,10,15]
print(sumEven(l1))

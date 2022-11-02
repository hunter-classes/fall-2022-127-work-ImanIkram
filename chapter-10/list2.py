
#4 Write a function called average that takes a list of numbers as a parameter and returns the average of the numbers.


def average(numlist):
    num_sum = 0 
    for num in numlist:
        num_sum = num_sum + num 
    avrg = num_sum / len(numlist)
    return avrg
    
print (average([3,3,3,3,3]))



#6 Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29



def sum_of_squares(xs):
    total = 0
    for sum_sqr in xs:
        total = total + sum_sqr **2  
    return total    
print (sum_of_squares([2,3,4]))
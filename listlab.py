'''Write a function to find the smallest value in a list'''

def min(l1):
    small = max(l1)
    for num in l1:
        if small > num:
            small = num
    return small
   

grades = [23,45,12,34,78,11,99,2]
print("minimum --> ", min(grades))    
   

'''Write a function that returns a new list that contains
    all the odd items in the original list'''
    
def odd_list(l2):
    odd = []
    for n in l2:
        if n % 2 != 0:
            odd.append(n)
    return odd
    
num = [1,2,3,4,5,6,7]   
print("odd_list -->" , odd_list(num))   


'''Write a function that takes a string and returns a new
    string where all the words are capitalized.'''
    
def capital_sent(sentence):
    result_list = []
    for word in sentence.split():
        new_word = word.capitalize()
        result_list.append(new_word)
    result = ""
    result = " ".join(result_list)
    return result

print ("capital_sent --> ", capital_sent("this is so amazing!"))
    
    
'''Write a function that takes a string and returns a new string
    with every word that's longer than 5 character turned into upper case'''

def upper(string):
    str1 = []
    for word in string.split():
        if len(word) > 5:
            upper_word = word.upper()
            str1.append(upper_word)        
    result = " "
    result = " ".join(str1)
    return result

print ("upper case -->" , upper("testing words more than five letters"))


'''Write a function that takes a list of numbers
    and returns a new list with each item squared'''


def num_sqr(lst):
    l1 = []
    for num in lst:
        l1.append(num**2)
    return l1
print("num_sqr --> ", num_sqr([1,2,3,4,5,6,7,8,9]))
    
    

'''Write a function that takes two lists of numbers and returns a new
    list where each item is the corresponding values of the original
    lists added together. Ex [1,2,3] and [10,20,30] would return the
    list [11,22,33]'''

'''def two_lists(lst1, lst2):
    lst3 = []
    for n in lst1:'''
        





'''chapter 10 # 10, 11, 12'''

   # 10 - Count how many words in a list have length 5.

def countWords(lst):
    word = 0
    for w in lst:
        if len(w) == 5:
            word = word + 1
    return word


fruits = ["apple", "banana", "grape", "orange", "peach"]
print("coutnWords with len 5 -->", countWords(fruits))

   # 11 - Sum all the elements in a list up to but not including the first even number.
   
   
   
   
   # 12 - Count how many words occur in a list up to and including the first occurrence of       the word “sam”.

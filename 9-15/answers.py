
# 7 Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

def is_even(n):
    if n%2 == 0:
      return True
    else:
      return False

print(is_even(19))

# 8 Now write the function is_odd(n) that returns True when n is odd and False otherwise.

def is_odd(n):
    if n%2 == 0:
      return False
    else:
      return True
      
print(is_odd(5))

#10 Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

def is_rightangled (a, b, c):
      if abs(a**2 + b**2 - c**2) < 0.001:
        return True
      else: 
        return False

print (is_rightangled(3.98,4,5))

#11
def is_rightangled2(a, b, c):
    if abs(c**2 + b**2 - a**2) < 0.001:
        return True
    elif abs(c**2 + a**2 - b**2) < 0.001: 
        return True 
    elif abs(a**2 + b**2 - c**2) < 0.001:
        return True
    else: 
        return False 
    
print (is_rightangled2(7.9,8.8,5))


##Do Coding Bat, Stirngs_1 "hello_name, make_out_word, and first_two.

def hello_name(name):
  return "Hello " + name + "!"

def make_out_word(out, word):
  return out[:2] + word + out[2:]

def first_two(str):
  return str[:2]



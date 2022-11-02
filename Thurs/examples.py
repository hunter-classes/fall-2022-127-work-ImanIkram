def is_even_short_version(n):
  return  n%2 == 0
      
def is_odd_short_version(n):
    return not (is_even_short_version(n))
      
print(is_odd_short_version(4))
result = is_odd_short_version(3)



def is_rightangled (a, b, c):
      if abs(a**2 + b**2 - c**2) < 0.001:
        return True
      else: 
        return False

def isRightAngle2 (a,b,c):
  """
  any order sides
  """
  return sRightAngle2 (a,b,c) or \
         sRightAngle2 (b,c,a) or \
         sRightAngle2 (a,c,b) 



def initialize(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "F. Last"
    """
    result = ""
    # isolate, uppercase and add first init to result
    first = name[0]
    first = first.upper()
    result = result + first + "."

    # find the last name (after space), cap it and add to result
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result = result + ' ' + last
    return result


    
# Test initialize
result = initialize("james bond")
print("james bond --> ",result)




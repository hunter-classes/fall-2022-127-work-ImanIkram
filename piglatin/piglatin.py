def bondify(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "Last, First Last"
    """
    
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result =  last + ","
     
    first = name.title()
 
    result = result + " " + first     
    return result

# Test Bondify
result = bondify("james bond")
print("james bond --> ",result)


#______________________________________________________________


def piglatin(word):
  """
input: a string representing a word
returns: a new string with the word converted to piglatin

Rules:
if the first letter is a consonent, move it from the start to the end and add "ay"
so "hello" becomes "ellohay"

If the first letter is a vowel, just add "yay" to the end

try to also handle upper case words
  """
  if word[0] in "a,e,i,o,u" :
    return word + "yay"
  else:
    return word [1:] + word[0] + "ay" 

# Test piglatin
result = piglatin("hello")
print(result)
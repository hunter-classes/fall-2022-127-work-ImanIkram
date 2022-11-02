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
  alphabets = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
  if word[0] in "a,e,i,o,u,A,E,I,O,U":
    word = word.capitalize()
    # checking if the last character is not an alphabet and is a            punctuation 
    if word[-1] not in alphabets:
      return word[:-1] + "yay" + word[-1]
    else: 
      return word + "yay"
  
  else:
    first = word[0]
    first = first.lower()
    second = word[1:-1]
    second = second.capitalize()
    if word[-1] not in alphabets:
      return second + first + "ay" + word[-1]
    else:
      return second + word[-1] + first + "ay" 
 
# Test piglatin
test_word = "cable."
result = piglatin(test_word)
print(test_word," -> ",result)

# Test piglatin
test_word1 = "cable"
result = piglatin(test_word1)
print(test_word1," -> ",result)

# Test piglatin
test_word2 = "Able."
result = piglatin(test_word2)
print(test_word2," -> ",result)



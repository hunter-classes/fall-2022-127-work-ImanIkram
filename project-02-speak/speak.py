# Extra completed: Handles punctuation
# Inserts pirate phrases at appropriate points in the document 

f = open("input.txt")
file = f.read()

# makes puncation a separate element 
file = file.replace(",", " , ").replace(".", " . ").replace("?", " ? ").replace("!", " ! ")
english = file.split()

# prints original input 
print(file)
print("\n")

dict = {"It's": "Tis",
        "to": "t'",
        "No": "Nay",
        "no": "nay",
        "old": "auld",
        "fishing": "fishin'",
        "the": "th'",
        "you": "ye",
        "beautiful": "fair",
        "What":"Wh't",
        "am":"be",
        "lake": "high seas",
        "get": "git",
        "fish": "bass",
        "boat": "barque", 
        "Besides": "Apart",
        "gather": "grab",
        "me": "my",
        "coming": "goin'"
}

# makes a list of keys 
keys = list(dict.keys())

# function to translate english to pirate     
def translate(english):
  pirate = []
  for word in english:
    if word in keys:
      pirate.append(dict[word])
    elif word == "<pirate>": # extra 
      pirate.append("Arrr")
    elif word == "<insult>": # extra 
      pirate.append("Ye lily-livered")
    else:
      pirate.append(word)   
  result = " ".join(pirate).replace(" !", "!").replace(" .",".").replace(" ,",",").replace(" ?", "?")
  return result
final = translate(english) 

#output
print(final)


"""
old code with an issue 
keys = list(dict.keys())
for word in keys:
    file = file.replace(word, dict[word])
print(file)"""






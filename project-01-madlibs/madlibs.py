'''Extras Completed:
    1. Write a story in a file and read it from your program.
    Make sure to include the file in your repo and that your program
    reads it correctly.
    2. Add some replacements that are unique, that is, the first
    time you see them you select on randomly but then you keep     
    reusing that replacement. 
'''

# Text File 
import random
file = open("data.txt")
data = file.read()


# Substitutions 
noun = ['night','nigthmare','planet','friendship','fear','clothes']
verb = ['camped','hiked','ate','slept','ran','cried','laughed','cooked']
adj = ['dark','crazy','odd','excited','lonely','absurd','hilarious']
char = ['Amanda', 'Aaleia','Alexa','Amelia','Ava']


# Function
def madlib(data):
    w = data
    w = w.replace('<char>', random.choice(char))
    for c in data:
        if c == '<':
            w = w.replace("<noun>", random.choice(noun), 1)
            w = w.replace("<verb>", random.choice(verb), 1)
            w = w.replace("<adj>", random.choice(adj), 1)            
    return w
    
file.close()

#Result 
print(madlib(data))


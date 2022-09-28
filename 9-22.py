#foreach Loop

for counter in range(5,21,5):
  print(counter)


for letter in "I am Iman":
  print(letter)


#while Loop

while False:
  print("this loop")
  print("will never end")

loop_counter = 0
while random.randrange(0,100)<80:
  print("Hello", loop_counter)
  loop_counter = loop_counter +1
print ("The above loop ran this many times: ", loop_counter)

#while loop as a counting loop
# first set up a variable to hold the count
i = 0
while i < 5:
  print (i)
  i = i+1


i = 5
while i > 5:
  print (i)
  i = i-1


s = "hello word"
i = 0
for i in range(len(s)):
  print(s[i])
  


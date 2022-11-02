# Add a new program named fizzbuzz.py. 
# When run, it should count from 1 to 100. 
# If the number is divisible by 3, print "fizz" if it's divisible by 5 print "buzz" and if it's divisible by 3 and 5, print "fizzbuzz"
# if it's not divisible by 3 or 5, print the number

for number in range(101):
    if number % 3 == 0 and number % 5 == 0: 
        print ("fizzbuzz") 
    elif number % 3 == 0:
        print ("fizz")
    elif number % 5 == 0: 
        print ("buzz") 
    else:
        print (number)  
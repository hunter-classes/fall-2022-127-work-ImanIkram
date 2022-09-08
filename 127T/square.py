import turtle
wn = turtle.Screen()
crush = turtle.Turtle()

## square function 

def square(crush):
  
  # draw a square
  for c in range(4):
    
    crush.forward(100)
    crush.left(90)
 
crush = turtle.Turtle()
square(crush)

squirt = turtle.Turtle()
squirt.penup()
squirt.goto(-100, -130)
squirt.pendown()
squirt.width(5)
squirt.color("red")       
square(squirt)  
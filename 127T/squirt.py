import turtle
wn = turtle.Screen()
crush = turtle.Turtle()

# draw a square
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)


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



  
## An equilateral triangle
triangle = turtle.Turtle()
triangle.shape("turtle")
triangle.color("red")
triangle.up()
triangle.goto(-100, 100)
triangle.down()
triangle.pensize(4)
for t in range(3):
    triangle.forward(100)
    triangle.left(120)




wn.exitonclick()
wn.mainloop()
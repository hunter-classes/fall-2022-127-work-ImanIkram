import turtle
wn = turtle.Screen()
crush = turtle.Turtle()

## square function 

def square(t, x,y, w, color, sidelen):
  """
  Draw a square using the turlte passed into t
  parameters:
  t -       a turle
  x,        y - location
  w -       width
  color -   color to draw in
  sidelen - length of each side
  Returns:
  nothing
  """
  
  ##set the location , color, and width
  t.penup()
  t.goto(x, y)
  t.width(w)
  t.color(color)
  t.pendown()
  # draw a square
  for c in range(4):
    t.forward(100)
    t.left(90)

crush = turtle.Turtle()
square(crush, 0,0, 1, "green", 50)

squirt = turtle.Turtle()       
square(squirt, -100, -100, 3, "red", 100) 

crush.setheading(45)
square(crush,150, 20,-100, "blue", 90)   
     


##def hexagon (t, x,y, color, sidelen):
  ##code to draw the triangle 
  
##def ngon (t, numsides, x,y, color, width, sidelen):
  ##code to draw ngon
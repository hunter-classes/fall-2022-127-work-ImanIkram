##def hexagon (t, x,y, color, sidelen):
  ##code to draw the hexagon 

import turtle
wn = turtle.Screen()

def hexagon (t, x,y, w, color, sidelen):
  ##code to draw the hexagon 
  t.penup()
  t.goto(x, y)
  t.width(w)
  t.color(color)
  t.pendown()
  # draw a hexagon
  for c in range(6):
    t.forward(sidelen)
    t.left(60)

sis = turtle.Turtle()
hexagon(sis, 0, 0, 3, "blue", 100)
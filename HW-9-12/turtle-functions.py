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



##code to draw ngon

def ngon (t, numsides, x,y, color, w, sidelen): 
   ##code to draw ngon 
  t.penup()
  t.goto(x, y)
  t.width(w)
  t.color(color)
  t.pendown()

  # draw a ngon
  for a in range (numsides):
    t.forward(sidelen)
    t.left(360/numsides)
    
poly = turtle.Turtle()
ngon(poly, 7, 0, -150, "blue", 5, 50)
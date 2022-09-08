  
  
##def ngon (t, numsides, x,y, color, width, sidelen):
  ##code to draw ngon


import turtle
wn = turtle.Screen()

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
ngon(poly, 7, 0, 0, "blue", 5, 50)
import turtle
wn = turtle.Screen()

def triangle (t, x,y, w, color, sidelen):
  ##code to draw the triangle 
  t.penup()
  t.goto(x, y)
  t.width(w)
  t.color(color)
  t.pendown()
  # draw a triangle
  for c in range(3):
    t.forward(sidelen)
    t.left(120)

bella = turtle.Turtle()
triangle(bella, 0, 0, 2, "red", 100)
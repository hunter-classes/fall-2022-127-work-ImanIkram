import turtle
wn = turtle.Screen()
pirate = turtle.Turtle()

wn.bgcolor ("yellow")
pirate.color("green")
pirate.pensize(3)

pirate.penup()
pirate.forward(65)
pirate.pendown()

for angles in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(angles)
    pirate.forward(100)
    
print(pirate.heading())
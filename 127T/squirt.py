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

## An equilateral triangle
triangle.shape("turtle")
triangle.color("red")
triangle.pensize(4)
for t in range(3):
    triangle.forward(100)
    triangle.left(120)



wn.exitonclick()
wn.mainloop()
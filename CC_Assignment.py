import turtle
turtle.bgcolor("black")

squary = turtle.Turtle()
squary.speed(20)
squary.pencolor("white")
for i in range(500):
    squary.forward(i)
    squary.left(50)

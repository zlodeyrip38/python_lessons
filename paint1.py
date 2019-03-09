import turtle

ninja = turtle.Turtle()

ninja.speed(10000)

for i in range(180):
    ninja.forward(100)
    ninja.right(50)
    ninja.forward(340)
    ninja.left(120)
    ninja.forward(80)
    ninja.right(9)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()
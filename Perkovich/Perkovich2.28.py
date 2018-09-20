import turtle

s = turtle.Screen()
t = turtle.Turtle()

x = 0
y = 0

t.penup()
t.goto(x, y + 80)
t.pendown()

t.pensize(3)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)

t.penup()
t.goto(x - 220, y + 50)
t.pendown()

t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)

t.penup()
t.goto(x, y - 160)
t.pendown()

t.left(360/8)
t.forward(100)
t.left(360/8)
t.forward(100)
t.left(360/8)
t.forward(100)
t.left(360/8)
t.forward(100)
t.left(360/8)
t.forward(100)
t.left(360/8)
t.forward(100)
t.left(360/8)
t.forward(100)
t.left(360/8)
t.forward(100)

s.exitonclick()
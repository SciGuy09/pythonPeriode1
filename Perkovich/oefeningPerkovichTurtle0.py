import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)

x = -100
y = 100
t.penup()
t.goto(x, y)
t.pendown()

t.circle(100)

t.penup()
t.goto(x - 35, y + 120)
t.pendown()
t.dot(25)

t.penup()
t.goto(x + 35, y + 120)
t.pendown()
t.dot(25)

t.penup()
t.goto(x - 60.63, y + 65)
t.pendown()
t.setheading(-60)
t.circle(70, 120)

help(turtle.Screen)
s.exitonclick()
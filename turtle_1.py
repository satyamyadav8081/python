import turtle
turtle.getscreen()
turtle.forward(100)
turtle.left(45)

turtle.forward(100)
turtle.rt(45)
turtle.forward(100)

turtle.bk(200)
turtle.shape("turtle")
print(turtle.shape())
import turtle

t = turtle.Turtle()
t.speed(5)

# Front square
for i in range(4):
    t.forward(100)
    t.left(90)

# Move to starting point for back square
t.penup()
t.goto(50, 50)
t.pendown()

# Back square
for i in range(4):
    t.forward(100)
    t.left(90)

# Connect front and back squares
t.penup()
t.goto(0, 0)
t.pendown()
t.goto(50, 50)

t.penup()
t.goto(100, 0)
t.pendown()
t.goto(150, 50)

t.penup()
t.goto(100, 100)
t.pendown()
t.goto(150, 150)

t.penup()
t.goto(0, 100)
t.pendown()
t.goto(50, 150)

turtle.done()
turtle.circle(100)

turtle.exitonclick()
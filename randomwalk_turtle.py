import turtle
from turtle import Turtle
import random
colors=["red","green","blue","orange","yellow","purple"]
turtle.colormode(255)
tom=Turtle()
tom.width(10)
tom.shape("turtle")
for _ in range(50):
 r=random.randint(0,255)
 g=random.randint(0,255)
 b=random.randint(0,255)
 tom.setheading(random.randrange(0,360,90))
 tom.pencolor((r,g,b))
 #tom.pencolor(random.choice(colors))
 tom.forward(30 )
tom.screen.mainloop()

#from turtle import Turtle,Screen
#tom=Turtle()
#s1=Screen()
#tom.color("red","yellow")
#print(tom.heading())
#tom.begin_fill()
#while True:
#for _ in range(50):
    #tom.forward(200)
    #tom.left(170)
    #if tom.heading()==0:
        #break   
#tom.end_fill()
#s1.exitonclick()

import random
import turtle
from turtle import Turtle,Screen
turtle.colormode(255)
tom=Turtle()
tom.speed("fastest")
s1=Screen()
while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tom.pencolor((r,g,b))
    tom.circle(100)
    tom.left(5)
    if tom.heading()==0:
     break
s1.exitonclick()
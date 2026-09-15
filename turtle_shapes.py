import random
from turtle import Turtle
tom=Turtle()
colors=["red","green","blue","orange","yellow","purple"]
for i in range(3,9): #3,4,5,6,7
    angle=360/i
    tom.pencolor(random.choice(colors)) 
    for _ in range(i): #1,2,3
        tom.forward(100)
        tom.rt(angle)
tom.screen.mainloop()        
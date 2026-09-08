#from turtle import exitonclick, forward, turtle
#abc=turtle()
#xyz=turtle()


#from turtle import*
#abc=Turtle()
#forward(100)
#exitonclick()

from turtle import Turtle, Screen
s1=Screen()
tom=Turtle()
for _ in range(15):
 tom.shape("turtle")
tom.pencolor("red")
tom. fillcolor("orange")
tom.begin_fill()
tom.circle(100)
tom.end_fill()
tom.rt(90)
tom.penup()
tom.forward(100)
tom.pendown()
tom.pensize(50)
tom.circle(50)
print(tom.pos())
tom.goto(-100,-100)
#tom.screen.mainloop()
#tom.color("red") 
s1.mainloop()
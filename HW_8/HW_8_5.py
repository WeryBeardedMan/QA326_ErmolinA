# для черепахи (из задания)

from turtle import *
speed(5)
pensize(2)
penup()
goto(-400, 0)
pendown()
colors = ["blue", "red", "black"]
for i in range(1, 13):
    pencolor(colors[i % 3])
    forward(50)
    penup()
    forward(20)
    pendown()
exitonclick()

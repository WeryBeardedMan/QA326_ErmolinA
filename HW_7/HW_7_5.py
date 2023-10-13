# напишите программу для черепахи, чтобы она рисовала
# вот так (в задании) (кол-во сторон произвольное)

from turtle import *
speed(5)
pensize(2)
penup()
goto(-400, 0)
pendown()
colors = ["blue", "red", "black"]
for i in range(1, 13):
    pencolor(colors[i % 3])
    forward(30)
    left(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    left(90)
exitonclick()

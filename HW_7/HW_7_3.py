# напишите программу для черепахи, чтобы она рисовала
# вот так  (кол-во углов произвольное)

from turtle import *
speed(5)
pensize(2)
penup()
goto(-300, -300)
pendown()
colors = ["orange", "black", "red", "blue"]
for i in range(1, 13):
    pencolor(colors[i % 4])
    left(90)
    forward(i*7)
    right(90)
    forward(i*7)
exitonclick()

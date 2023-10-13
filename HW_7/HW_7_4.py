# напишите программу для черепахи, чтобы она рисовала вот так (в задании)
# (кол-во сторон произвольное)
# Квадратная спираль с чередующимеся цветами сторон

from turtle import *
speed(5)
pensize(2)
colors = ["blue", "red", "green"]
for i in range(1, 31):
    pencolor(colors[i % 3])
    forward(i*10)
    left(90)
exitonclick()

# Используя модуль turtle, и создав функцию рисования квадрата, решите следующую задачу:
# (квадрат из квадратов - из задания)
#
# все квадраты одинакового размера

from turtle import *

speed(5)
pensize(2)


def draw_square(a):
    for i in range(4):
        forward(a)
        left(90)


for a in range(200, 0, -40):
    draw_square(a)
penup()
goto(200, 200)
pendown()
left(180)
for a in range(200, 0, -40):
    draw_square(a)
exitonclick()

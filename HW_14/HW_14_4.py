# Написать функцию для фигуры как на картинке.
# (фигура из задания)
# и решить задачу с применением этой функции

from turtle import *

speed(4)
pensize(2)
decagon = 10
pentagon = 5


def draw_decagons(l_d):
    for j in range(10):
        for i in range(decagon):
            forward(l_d)
            right(360 / decagon)
        right(360 / decagon)


def draw_pentagon(l_p):
    for j in range(10):
        for i in range(pentagon):
            forward(l_p)
            right(360 / pentagon)
        right(360 / decagon)


pencolor("blue")
draw_decagons(40)
pencolor("red")
draw_pentagon(80)
exitonclick()

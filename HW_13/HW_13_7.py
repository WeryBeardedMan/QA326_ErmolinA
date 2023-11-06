# Используя модуль turtle и, создав функцию рисования шестиугольника, решите следующую задачу:
# (фигура из задания)
# Все шестиугольники одинакового размера.
#

from turtle import *

speed(1)
pensize(2)


def draw_hexagon(a):
    for i in range(6):
        forward(a)
        left(360 / 6)


draw_hexagon(80)
left(180)
draw_hexagon(80)
forward(80)
right(120)
draw_hexagon(80)
exitonclick()

# Используя модуль turtle и, создав функцию рисования квадрата, решите следующую задачу:
# (фигура из задания)
#
# Все треугольники одинакового размера. Для треугольника можно использовать функцию из классной работы.

from turtle import *

speed(1)
pensize(2)


def draw_triangle(a):
    for i in range(3):
        forward(a)
        right(120)


def draw_square(a):
    for i in range(4):
        forward(a)
        left(90)
        draw_triangle(80)


draw_square(80)
exitonclick()

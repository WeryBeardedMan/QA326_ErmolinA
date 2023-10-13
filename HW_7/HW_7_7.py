# Дано:
# n - кол-во сторон (гарантируется, что число целое)
# a - сторона многоугольника
# is_fill - нужно залить фигуру (гарантируется, что
# будет использован только логический тип данных)
# нарисовать ПРАВИЛЬНЫЙ многоугольник по заданным
# характеристикам
# УСЛОЖНЕНИЕ(необязательно делать) (добавьте еще одну переменную,
# хочет ли пользователь, чтобы каждая сторона многоугольника была разного цвета)

from random import randint
from turtle import*
a = int(input("Введите количество сторон многоугольника: "))
n = int(input("Введите длину стороны многоугольника: "))
is_fill = int(input("Хотите залить фигуру? Введите 1 - если хотите и 0, если нет: "))
is_fill = bool(is_fill)
colors_side = int(input("""Хотите ли чтобы стороны многоугольника были разных цветов?
Введите 1 - если хотите и 0, если нет: """))
colors_side = bool(colors_side)
if is_fill:
    pensize(6)
    fillcolor("purple")
    begin_fill()
    if colors_side:
        for i in range(a):
            colormode(255)
            pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
            forward(n)
            right(360 - (360/a))
    else:
        for i in range(a):
            forward(n)
            right(360 - (360 / a))
    end_fill()
else:
    if colors_side:
        pensize(6)
        for i in range(a):
            colormode(255)
            pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
            forward(n)
            right(360 - (360/a))
    else:
        pensize(6)
        for i in range(a):
            forward(n)
            right(360 - (360 / a))
exitonclick()

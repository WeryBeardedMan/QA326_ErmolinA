# Пользователь вводит желаемую фигуру (“круг”, “квадрат”, “прямоугольник”, “треугольник”)
# Нарисовать данную фигуру при помощи модуля turtle
# Пользователь выбирает хочет ли он закрасить круг или нет.
# В зависимости от выбора пользователя нарисовать при помощи модуля turtle закрашенный круг или полый круг
# Несколько доработал - объединил 2 задачи, теперь программа рисует закрашенные или незакрашенные фигуры по запросу
#
print("Введите название фигуры, в формате 'круг' 'квадрат' 'прямоугольник' 'треугольник', без кавычек")
figure = str(input())
print("Нужно ли закрашивать фигуру? Введите без кавычек '1' если нужно закрасить и '0', если закрашивать не нужно")
paint_over = int(input())
import turtle
pen = turtle.Turtle()
if figure == 'круг' and paint_over == 1:
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
else:
    if figure == 'круг' and paint_over == 0:
        pen.circle(100)
if figure == 'квадрат' and paint_over == 1:
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.end_fill()
else:
    if figure == 'квадрат' and paint_over == 0:
        pen.left(90)
        pen.forward(100)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
        pen.forward(100)
if figure == 'прямоугольник' and paint_over == 1:
    pen.fillcolor("green")
    pen.begin_fill()
    pen.left(90)
    pen.forward(160)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(160)
    pen.left(90)
    pen.forward(100)
    pen.end_fill()
else:
    if figure == 'прямоугольник' and paint_over == 0:
        pen.left(90)
        pen.forward(160)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
        pen.forward(160)
        pen.left(90)
        pen.forward(100)
if figure == 'треугольник' and paint_over == 1:
    pen.fillcolor("brown")
    pen.begin_fill()
    pen.left(120)
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.end_fill()
else:
    if figure == 'треугольник' and paint_over == 0:
        pen.left(120)
        pen.forward(100)
        pen.left(120)
        pen.forward(100)
        pen.left(120)
        pen.forward(100)
import time
time.sleep(3)

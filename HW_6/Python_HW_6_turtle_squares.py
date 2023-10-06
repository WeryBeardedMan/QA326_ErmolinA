# написать программу для черепашки, рисуем квадраты вокруг квадратов
from turtle import*
import time
side = 40
indent = 20
for i in range(6):
    for j in range(4):
        forward(side)
        left(90)
    penup()
    right(90)
    forward(indent)
    left(90)
    backward(indent)
    pendown()
    side += indent * 2
time.sleep(10)

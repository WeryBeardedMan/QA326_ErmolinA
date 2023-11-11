# Написать ОДНУ функцию для фигур как на картинке
# и решить задачу с применением этой функции. Порядок фигур не важен.
# Также должна быть возможность задавать произвольный размер и цвет через функцию

from turtle import *


def draw_random_polygons(side=int(), angles_of_polygon=int(), color_polygon=str(), x=int(), y=int()):
    penup()
    goto(x, y)
    pendown()
    pencolor(color_polygon)
    fillcolor(color_polygon)
    begin_fill()
    for i in range(angles_of_polygon):
        fillcolor(color_polygon)
        forward(side)
        right(360 / angles_of_polygon)
    end_fill()


draw_random_polygons(20, 11, 'brown', -370, 270)
draw_random_polygons(30, 7, 'deep pink', -250, 150)
draw_random_polygons(75, 3, 'red', -130, 30)
draw_random_polygons(40, 6, 'cyan', -10, -90)
draw_random_polygons(25, 10, 'pink', 110, -210)
draw_random_polygons(30, 8, 'black', 110, 270)
draw_random_polygons(60, 4, 'green', -10, 150)
draw_random_polygons(45, 5, 'blue', -250, -90)
draw_random_polygons(27, 9, 'yellow', -370, -210)
exitonclick()

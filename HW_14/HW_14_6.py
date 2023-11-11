# Можно решить задачу как одной функцией, так и двумя и более. Главное, чтобы получился результат
# как на картинке. Функция должна принимать произвольный размер снежинки,
# произвольное кол-во сегментов и произвольный цвет

from turtle import *

speed(5)


def snowflake_ray(count_of_ray=int(), snowflake_color=str(), segment_size=int()):
    pensize_value = int(segment_size/10)   # масштабирую толщину линии к длине сегмента
    pensize(pensize_value)
    pencolor(snowflake_color)
    for i in range(count_of_ray):
        forward(segment_size)
        right(60)
        for j in range(3):
            forward(segment_size/2)
            backward(segment_size/2)
            left(60)
        right(120)
        backward(segment_size)
        left(60)


snowflake_ray(6, 'silver', 90)
exitonclick()

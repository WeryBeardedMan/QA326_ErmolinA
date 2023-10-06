# Запросить координаты точки (x, y) и определить номер четверти, в которую попала эта точка.
# Необходимо учесть случаи попадания точки на оси X или Y или в начало координат.
#
print("Введите координаты точки по оси X:")
x_coordinate = float(input())
print("Введите координаты точки по оси Y:")
y_coordinate = float(input())
if x_coordinate > 0 and y_coordinate > 0:
    print("Указанная точка находится в I четверти")
elif x_coordinate < 0 and y_coordinate > 0:
    print("Указанная точка находится во II четверти")
elif x_coordinate < 0 and y_coordinate < 0:
    print("Указанная точка находится в III четверти")
elif x_coordinate > 0 and y_coordinate < 0:
    print("Указанная точка находится в IV четверти")
elif x_coordinate == 0 and y_coordinate == 0:
    print("Указанная точка находится в начале координат")
elif x_coordinate == 0:
    print("Указанная точка находится на оси Y")
elif y_coordinate == 0:
    print("Указанная точка находится на оси X")

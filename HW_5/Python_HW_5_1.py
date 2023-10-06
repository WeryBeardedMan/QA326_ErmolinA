# 3 стороны треугольника
# Проверить существует ли треугольник

side_a = float(input("Введите 1 сторону треугольника:"))
side_b = float(input("Введите 2 сторону треугольника:"))
side_c = float(input("Введите 3 сторону треугольника:"))
if side_a > 0 and side_b > 0 and side_c > 0:
    if (side_a + side_b) > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        print("Треугольник существует.")
    else:
        print("Такого треугольника не существует.")
else:
    print("Стороны треугольника не могут быть нулевыми или отрицательными!")

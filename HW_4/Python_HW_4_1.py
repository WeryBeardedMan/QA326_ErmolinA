# задача 1
# даны 3 числа, распечатать в порядке возрастания
#
print("Введите 3 числа (могут быть любыми в том числе дробными). Программа расставит их в порядке ворзастания.")
num_1 = float(input("Введите первое число: "))
num_2 = float(input("PВведите второе число: "))
num_3 = float(input("Pвведите третье число: "))
if num_1 < num_2 and num_3 < num_2:
    if num_1 > num_3:
        print(num_3, num_1, num_2)
    else:
        print(num_1, num_3, num_2)
elif num_1 < num_3 and num_2 < num_3:
    if num_1 > num_2:
        print(num_2, num_1, num_3)
    else:
        print(num_1, num_2, num_3)
elif num_2 < num_1 and num_3 < num_1:
    if num_3 > num_2:
        print(num_2, num_3, num_1)
    else:
        print(num_3, num_2, num_1)
else:
    print(num_1, num_2, num_3)

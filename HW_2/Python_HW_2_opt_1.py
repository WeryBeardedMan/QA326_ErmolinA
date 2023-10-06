# Вывести на экран число(может быть любым), если последняя цифра числа равна 8
#
print("Введите число:")
input_num = float(input())
last_digit = abs(input_num) % 10
if last_digit == 8:
    print(f"Число {input_num} заканчивается на 8")
else:
    print("Введенное число не заканчивается на 8")

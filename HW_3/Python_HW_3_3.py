# Дано два числа. Найдите наибольшее четное число среди них. Если оно не существует, выведите фразу "not found".
#
print("Введите первое число (целое):")
num_1 = int(input())
print("Введите второе число (целое):")
num_2 = int(input())
if num_1 % 2 == 0 and num_2 % 2 == 0:
    if num_1 > num_2:
        print(f"Наибольшее четное число среди введенных чисел: {num_1}")
    elif num_2 > num_1:
        print(f"Наибольшее четное число среди введенных чисел: {num_2}")
    elif num_1 == num_2:
        print(f"Введенные числа равны.")
else:
    print("not found")

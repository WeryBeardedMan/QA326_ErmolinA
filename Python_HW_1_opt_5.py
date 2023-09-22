# Дано произвольное число. Найти произведение уникальных цифр.
# 123
# 1*2*3=6
# 1223
# 1*2*3=6
# ввод 1
# вывод 1
#
print("Введите целое число:")
input_num = int(input())
list_numbers = [int(i) for i in str(input_num)]
unique_numbers = list(set(list_numbers))
print("Список уникальных цифр введенного числа", unique_numbers)
import math
result = math.prod(unique_numbers)
print("Результат произведения уникальных цифр введенного числа:", result)

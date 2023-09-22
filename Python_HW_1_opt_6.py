# Дано 4-хзначное число, найдите его 2-ой максимум.
# Пример:
# 1234
# 3
# 4612
# 4
#
print("Введите целое число:")
input_num = int(input())
list_numbers = [int(i) for i in str(input_num)]
list_numbers.sort()
max_number = list_numbers[0]
for number in list_numbers:
    if number > max_number:
        max_number = number
# # Вывод максимального числа
# print("Первый максимум в числе:", max_number)
# # удаляем первый максимум числа
value_to_remove = max_number
while value_to_remove in list_numbers:
    list_numbers.remove(value_to_remove)
if list_numbers != []:
    print("Второй максимум в числе:", list_numbers[-1])
else:
    print("У числа нет второго максимума")

# дан список
# запрещено использовать sort, max, count, map преобразовывать список
# в другие типы тоже нельзя
# найти элемент(ы) в списке, который повторяется дважды и более раз

# 1) реализовал заполнение списка numbers с помощью random
# 2) ищу не уникальные элементы заданного списка перебором значений и
# формирую новый список всех элементов, имеющих совпадения (не вывожу его на печать, закомментировал в коде,
# но оставил для наглядности)
# 3) из полученного списка не уникальных значений перебором формирую новый список, исключая повторения
#
#                         замороченно ;))

from random import *
numbers = []
unique = True
not_unique_numbers = []
result = []
n = 35
for i in range(n):
    numbers.append(randint(0, 20))
print(f"Сформирован список: {numbers}")
for i in range(n - 1):
    for j in range(i + 1, n):
        if numbers[i] == numbers[j]:
            not_unique_numbers.append(numbers[i])
            unique = False
for el in not_unique_numbers:
    if el not in result:
        result.append(el)
if unique:
    print("Все элементы уникальны")
else:
    # print(f"Элементы заданного списка, повторяющиеся 2 и более раз: {not_unique_numbers}")
    print(f"Элементы заданного списка, повторяющиеся 2 и более раз: {result}")

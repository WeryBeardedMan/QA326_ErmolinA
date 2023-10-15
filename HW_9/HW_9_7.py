# дан список
# запрещено использовать sort, max, count, sum, map,
# преобразовывать список в другие типы тоже нельзя
# найти произведение всех элементов в этом списке

# реализовал заполнение списка с помощью random

from random import *
numbers = []
n = 3
for i in range(n):
    numbers.append(randint(0, 12))
print(f"Сформирован список: {numbers}")
mult_numbers = 1
for element in numbers:
    mult_numbers = element * mult_numbers
print(f"Произведение элементов в данном списке: {mult_numbers}")

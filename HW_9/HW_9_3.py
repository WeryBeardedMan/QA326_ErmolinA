# # дан  список
# запрещено использовать sort, max, count, sum, map
# сформировать новый список, с положительными числами

# реализовал заполнение списка с помощью random

from random import *
numbers = []
n = 12
for i in range(n):
    numbers.append(randint(-100, 100))
print(f"Сформирован список: {numbers}")
positive_numbers = []
for element in numbers:
    if element > 0:
        positive_numbers.append(element)
print(f"Список, содержащий только положительные значения из заданного списка: {positive_numbers}")

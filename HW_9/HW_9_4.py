# дан список
# запрещено использовать sort, max, count, sum, map
# удалить из этого списка, все отрицательные элементы

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
        numbers = positive_numbers
print(f"Список элементов после удаления отрицательных значений: {numbers}")

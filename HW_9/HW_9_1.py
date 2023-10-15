# дан  список
# запрещено использовать sort, max, map преобразовывать список
# в другие типы тоже нельзя
# найти минимальный элемент в списке

# реализовал заполнение списка с помощью random

from random import *
numbers = []
n = 12
min_el = int()  # объявил переменную, потому что PyCharm ругался, что переменная не объявлена
for i in range(n):
    numbers.append(randint(-100, 100))
    min_el = numbers[0]
    for element in numbers:
        if element < min_el:
            min_el = element
print(f"Сформирован список: {numbers}")
print(f"Минимальный элемент в данном списке: {min_el}")

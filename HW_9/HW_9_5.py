# дан список
# найти все элементы в этом списке, из которых извлекается квадратный
# корень в виде целого числа (4, 16 и т.д.)

from math import sqrt
from random import *
numbers = []
n = 30
for i in range(n):
    numbers.append(randint(0, 100))
print(f"Сформирован список: {numbers}")
square_root_numbers = []
nums = 0
for element in numbers:
    nums = sqrt(element)
    if nums % 1 == 0:
        square_root_numbers.append(element)
print(f"Элементы списка, из которых можно извлечь квадратный корень в виде целого числа: {square_root_numbers}")

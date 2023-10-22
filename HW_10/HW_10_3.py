# В данном массиве найти два наименьших элемента.

# реализовал заполнение массива с помощью random

import random
numbers = [random.randint(-40, 40) for i in range(20)]
print(f"Сформирован массив чисел: {numbers}")
unique_numbers = list(set(numbers))
unique_numbers.sort()
print(f"Два наименьших элемента в заданном массиве: {unique_numbers[0]}, {unique_numbers[1]}")

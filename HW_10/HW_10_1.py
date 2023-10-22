# Найдите количество различных элементов данного массива.

# реализовал заполнение массива с помощью random

import random
numbers = [random.randint(0, 15) for i in range(20)]
counter = 0
for i in range(len(numbers)):
    if not numbers[i] in numbers[0:i]:
        counter += 1
print(f"Сформирован массив чисел: {numbers}")
print(f"Количество различных элементов заданного массива: {counter}")

# Написать функцию is_positive(num), которая возвращает True в случае, если num положительное,
# и False во всех остальных случаях.
# Дан список чисел (только целые числа).
# Напечатать 0 и отрицательные числа в списке применив, функцию is_positive

import random
def is_positive(num):
    if num <= 0:
        return False
    else:
        return True
numbers_list = [random.randint(-15, 15) for i in range(20)]
negative_numbers = []
for num in numbers_list:
    if not is_positive(num):
        negative_numbers.append(num)
print(f"Сформирован список: {numbers_list}")
print(f"После извлечения из списка положительных значений: {negative_numbers}")

# Дан список чисел (можно создать любым способом, но приветствуется через лямбду функцию и random).
# Создать новый список при помощи filter(), отобрать значения по маске (3*3?), где * - любое кол-во цифр, ? - одна цифра
# Вычислить при помощи reduce() произведение нового списка.

import random
import re
import functools

num_list = []
random_num = lambda: random.randint(0, 9999)
for i in range(123):
    num_list.append(random_num())
num_list = list(map(str, num_list))
print(num_list)
reg_ex = re.compile(r'^3\d*3\d$')
valid_numbers = list(filter(reg_ex.match, num_list))
if valid_numbers:
    print(f'Список чисел, отвечающих условию: {valid_numbers}')
    if len(valid_numbers) >= 2:
        valid_numbers = list(map(int, valid_numbers))
        product_of_numbers = functools.reduce(lambda x, y: x * y, valid_numbers)
        print(f'Произведение чисел, отвечающих условию: {product_of_numbers}')
    else:
        print('Список состоит из 1 числа. Перемножать нечего.')
else:
    print('Не найдено чисел, отвечающих условию.')

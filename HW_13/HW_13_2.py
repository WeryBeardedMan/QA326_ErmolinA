# Дана строка с - произвольная строка.
#
# Написать регулярное выражение для определения номера автомобиля.
# Допускается только такая запись номера автомобиля А000АА.
# А-любая буква(латиница)
# 0-любая цифра
#
# Программа должна вывести кол-во валидных значений и показать их в консоли.

import re

auto_numbers = """
A000AA
B983AR
G948FD
!@#$%%^&
00000000
00 00 0 00 00
__________
Ы674ПЮ
F999IZ
"""
reg_ex = r'[A-Z]{1}\d{3}[A-Z]{2}'
numbers = re.findall(reg_ex, auto_numbers)
print("Валидные значения:")
i = 0
for num in numbers:
    i += 1
    print(f"{i}: {num}")
print(f"Количество валидных значений всего: {i}")

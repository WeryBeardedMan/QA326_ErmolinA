# Дана произвольная строка. Создать строку, в которой содержаться только цифры из исходной строки.
# Пример:
# ввод: АА”АА324А К*К№5 10 79
# вывод:32451079

import string
import random
characters = 120
random_row = ''.join(random.choices(string.ascii_uppercase
                                    + string.digits + string.ascii_lowercase
                                    + string.punctuation
                                    + string.whitespace,  k=characters))
print(f'Сгенерирована строка: {random_row}')
nums_row = [num for num in filter(lambda num: num.isdigit(), random_row)]
print(f'Строка, содержащая только цифры из сгенерированной строки: {''.join(map(str, nums_row))}')

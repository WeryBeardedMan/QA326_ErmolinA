# Сделайте функцию, которая параметром будет принимать букву и проверять, это буква кириллицы или латиницы.

import re


def define_alphabet(text):
    if text in re.findall('[ЯЁА-яёа]', text):
        print('Это буква кириллицы.')
    elif text in re.findall('[a-zA-Z]', text):
        print('Это буква латинского алфавита.')


text = str(input('Введите 1 букву: '))
if text.isalpha() and len(text) == 1:
    define_alphabet(text)
else:
    (print('Введена не буква, либо не верное количество символов, либо буква не кириллицы и не латиницы.'))

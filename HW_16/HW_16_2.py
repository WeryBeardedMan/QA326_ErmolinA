# Дан текстовый файл. Написать функцию, которая составляет шифр для цифр (шифр можете придумать свой,
# вот пример 1 → ! | 2 → @ | 3 → # | 4 → $ и т.д.), возвращаемое значение должно быть типа string.
# Применить эту функцию для файла и заменить все цифры на зашифрованные значения.


def crypting_lines():
    global lines
    code_dictionary = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
                       '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
    for i in code_dictionary:
        lines = lines.replace(i, code_dictionary[i])
    return lines


with open('16_2_line.txt', 'r+') as f:
    lines = f.read()
    f.seek(0)
    f.write(f'Test string before crypting: {lines} \n' + f'Test string after crypting: {crypting_lines()}')

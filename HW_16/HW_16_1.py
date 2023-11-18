# Дан текстовый файл. Написать функцию, которая будет подсчитывать количество чисел в строке,
# числа отделены пробелами, возвращаемое значение должно быть типа int().
# Применить эту функцию для файла и найти общее кол-во таких чисел

with open('16_1_line.txt', 'r') as f:
    lines = f.read()
numbers = lines.split()
numbers = len(list(filter(lambda num: num.isdigit(), numbers)))
print(f'Количество чисел в файле 16_1_line.txt равно: {numbers}')

# Напишите функцию, которая будет принимать числа (может быть разное кол-во)
# и находить среднее арифметическое для данного набора.

def find_arithmetic_mean():
    sum = 0
    numbers_count = len(num_list)
    for i in num_list:
        sum += i
    arithmetic_mean_list = sum/numbers_count
    return arithmetic_mean_list


try:
    num_list = list(map(int, input('Введите целые числа в одну строку через пробелы: ').split()))
    if len(num_list) >= 2:
        print(f'Среднее арифметическое введенных чисел: {find_arithmetic_mean()}')
    else:
        print('Введено одно число, либо введены символы табуляции.')
except ValueError:
    print('Перечитайте условия ввода.')

# Игра угадай число от 1 до 100
# реализовать подсказки (число введенное больше или меньше).
# Сделать проверку на ввод числа для пользователя (может быть абсолютно любой символ)

import time
import random
comp_choise = random.randint(1, 100)
print("Игра угадай число от 1 до 100! Правила: Вводите числа от 1 до 100, пока не угадаете, будут даны подсказки!")
while True:
    try:
        human_choice = int(input("Введите число: "))
    except ValueError:
        print("Введено не число!")
        continue
    else:
        if human_choice < comp_choise:
            print("Введенное число меньше загаданного!")
        elif human_choice > comp_choise:
            print("Введенное число больше загаданного!")
        elif human_choice == comp_choise:
            print("Вы наконец-то угадали число!")
            time.sleep(3)
            break

# задача 3
# Игра камень ножницы бумага с компьютером
# (камень побеждает ножницы / ножницы побеждает бумагу / бумага побеждает камень)
# Игрок делает ход и затем компьютер делает ход
# Вывести кто победил.
#
import random
import time
print("""'Игра "Камень/ножницы/бумага": Сделайте ход - введите число от 1 до 3,
где 1 - "Камень", 2 - "Ножницы", 3 - "Бумага"'""")
human_choice = int(input())
if human_choice >= 1 and human_choice <= 3:
    if human_choice == 1:
        print('Игрок сделал ход и выкинул "Камень", компьютер делает ход.')
    elif human_choice == 2:
        print('Игрок сделал ход и выкинул "Ножницы", компьютер делает ход.')
    elif human_choice == 3:
        print('Игрок сделал ход и выкинул "Бумага", компьютер делает ход.')
    time.sleep(2)
    comp_choice = random.randint(1, 3)
    if comp_choice == 1 and human_choice == 1:
        print('Ничья, оба игрока выбросили "Камень"')
    elif comp_choice == 2 and human_choice == 2:
        print('Ничья, оба игрока выбросили "Ножницы"')
    elif comp_choice == 3 and human_choice == 3:
        print('Ничья, оба игрока выбросили "Бумага"')
    elif comp_choice == 1 and human_choice == 2:
        print('Компьютер выбросил "Камень" - победил компьютер')
    elif comp_choice == 1 and human_choice == 3:
        print('Компьютер выбросил "Камень" - победил игрок')
    elif comp_choice == 2 and human_choice == 1:
        print('Компьютер выбросил "Ножницы" - победил игрок')
    elif comp_choice == 2 and human_choice == 3:
        print('Компьютер выбросил "Ножницы" - победил компьютер')
    elif comp_choice == 3 and human_choice == 1:
        print('Компьютер выбросил "Бумага" - победил компьютер')
    elif comp_choice == 3 and human_choice == 2:
        print('Компьютер выбросил "Бумага" - победил игрок')
else:
    print('Игрок не понял условий. Возможно игра слишком сложная и стоит поискать что-то попроще.')

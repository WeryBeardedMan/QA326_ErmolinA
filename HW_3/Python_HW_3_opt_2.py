# Робот может перемещаться в четырех направлениях («11» — север, «12» — запад, «13» — юг, «14» — восток)
# и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, –1 — поворот направо.
# Дано число (11, 12, 13 или 14) — исходное направление робота и целое число N (0, 1 или -1) — посланная ему команда.
# Вывести направление робота после выполнения полученной команды (то есть север, запад, юг или восток).
#
print("""Введите целое число от 11 до 14, определяющее исходное положение робота,
где «11» — север, «12» — запад, «13» — юг, «14» — восток""")
orientation = int(input())
print('Введите  команду на движение робота, где 0 — продолжать движение, 1 — поворот налево, –1 — поворот направо')
N = int(input())
if 11 <= orientation <= 14 and (N == 1 or N == 0 or N == -1):
    if orientation == 11 and N == 0:
        print("Направление робота: север")
    elif orientation == 11 and N == 1:
        print("Направление робота: запад")
    elif orientation == 11 and N == -1:
        print("Направление робота: восток")
    elif orientation == 12 and N == 0:
        print("Направление робота: запад")
    elif orientation == 12 and N == 1:
        print("Направление робота: юг")
    elif orientation == 12 and N == -1:
        print("Направление робота: север")
    elif orientation == 13 and N == 0:
        print("Направление робота: юг")
    elif orientation == 13 and N == 1:
        print("Направление робота: восток")
    elif orientation == 13 and N == -1:
        print("Направление робота: запад")
    elif orientation == 14 and N == 0:
        print("Направление робота: восток")
    elif orientation == 14 and N == 1:
        print("Направление робота: север")
    elif orientation == 14 and N == -1:
        print("Направление робота: юг")
else:
    print("Введены не верные команды для робота.")
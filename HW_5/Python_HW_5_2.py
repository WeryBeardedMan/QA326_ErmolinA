# кол-во из чего переводим: часов, минут, секунд (что-то одно на выбор пользователя)
# кол-во во что переводим: часов, минут, секунд (что-то одно на выбор пользователя)
# реализовать интерфейс для перевода из (часов, минут, секунд) в (часов, минут, секунд)

from_what = str(input("""Введите еденицу измерения времени из которой хотите переводить (без кавычек).
Введите 'h' - для часов, 'm' - для минут и 's' - для секунд: """))
if from_what == 'h' or from_what == 'm' or from_what == 's':
    time = float(input("""Введите значение выбранного для перевода времени.
Вводите не отрицательное значение: """))
    if time > 0:
        into_what = str(input("""Введите еденицу измерения времени в которую хотите перевести
Введите 'h' - для часов, 'm' - для минут и 's' - для секунд: """))
        if into_what == 'h' or into_what == 'm' or into_what == 's':
            if from_what == 'h' and into_what == 'h':
                print("Значение осталось прежним, т.к. переводим часы в часы")
            elif from_what == 'h' and into_what == 'm':
                result = float(time * 60)
                print(f"{time} hour = {result} minute")
            elif from_what == 'h' and into_what == 's':
                result = float(time * 3600)
                print(f"{time} hour = {result} second")
            elif from_what == 'm' and into_what == 'm':
                print("Значение осталось прежним, т.к. переводим минуты в минуты")
            elif from_what == 'm' and into_what == 'h':
                result = float(time / 60)
                print(f"{time} minute = {result} hour")
            elif from_what == 'm' and into_what == 's':
                result = float(time * 60)
                print(f"{time} minute = {result} second")
            elif from_what == 's' and into_what == 's':
                print("Значение осталось прежним, т.к. переводим секунды в секунды")
            elif from_what == 's' and into_what == 'm':
                result = float(time / 60)
                print(f"{time} second = {result} minute")
            elif from_what == 's' and into_what == 'h':
                result = float(time / 3600)
                print(f"{time} second = {result} hour")
        else:
            print("Вы ввели неверные данные, перечитайте условия ввода!")
    else:
        print("Вы ввели отрицательные значения времени")
else:
    print("Вы ввели неверные данные, перечитайте условия ввода!")

# дорешать задачу используя конструкции match case
# код: https://github.com/makarova1507ana/qa_326
# /blob/main/%D0%B4%D0%BB%D1%8F%20%D0%B4%D0%B7%20%D1%84%D0%B0%D0%B9%D0%BB%D1%8B/match_case.py

#  -------------------------ЗАДАЧА-----------------------------#
# Перевод Из мм в м, из м в км (и наоборот)

from_what = str(input("Из чего переводим? mm, m или km: "))  # из которого делается перевод
length = int(input("Значение: "))  # добавьте проверку на >=0
into_what = str(input("Во что переводим? mm, m или km: "))  # в который делается перевод
if length >= 0:
    match from_what:
        case 'm':
            match into_what:
                case 'km':
                    print(f"Результат перевода: {length / 1000}")
                case _:
                    pass
        case 'km':
            match into_what:
                case 'm':
                    print(f"Результат перевода: {length * 1000}")
                case _:
                    pass
    match from_what:
        case 'mm':
            match into_what:
                case 'm':
                    print(f"Результат перевода: {length / 100}")
                case _:
                    pass
        case 'm':
            match into_what:
                case 'mm':
                    print(f"Результат перевода: {length * 100}")
                case _:
                    pass
else:
    print("Вы ввели отрицательное значение длины.")

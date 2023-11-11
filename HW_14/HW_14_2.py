# написать функцию num_to_name_week(num_day_week), которая возвращает имя дня недели(строка)
# Пример: num_to_name_week(1) -> ‘Понедельник’

day_of_week = {1: 'Понедельник',
               2: 'Вторник',
               3: 'Среда',
               4: 'Четверг',
               5: 'Пятница',
               6: 'Суббота',
               7: 'Воскресенье'}
result = str()
num_day = int()


def num_day_week():
    global day_of_week, result, num_day
    try:
        num_day = int(input('Введите номер дня недели (дней недели всего 7), программа напечатает название дня: '))
        if num_day in day_of_week:
            result = day_of_week.get(num_day)
            return result
        else:
            print(f"В неделе всего 7 дней!")
    except ValueError:
        print('Вы ввели не верное значение дня недели! Пожалуйста, перечитайте условия ввода!')


num_day_week()
print(result)

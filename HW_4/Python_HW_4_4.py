# Пользователь с клавиатуры вводит количество часов.
# Если полученное значение находится в диапазоне от 0 до 5 нужно вывести надпись Good Night,
# если в диапазоне от 6 до 13 Good Morning, если в диапазоне от 13 до 17 Good Day,
# если в диапазоне от 17 до 0 Good Evening.

time_of_day = int(input("Введите сколько сейчас часов (в сутках 24 часа): "))
if time_of_day >= 0 and time_of_day < 24:
    if time_of_day >= 0 and time_of_day <= 5:
        print("Good Night!")
    elif time_of_day >= 6 and time_of_day < 13:
        print("Good Morning!")
    elif time_of_day >= 13 and time_of_day < 17:
        print("Good Day!")
    elif time_of_day >= 17 and time_of_day <= 23:
        print("Good Evening!")
else:
    print("You didn't understand the task.")

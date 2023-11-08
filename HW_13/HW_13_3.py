# Написать регулярное выражение для определения валидных логинов.
# Валидными считаются те логины, которые удовлетворяют следующим условиям:
# ●	содержится минимум 1 букву латинского алфавита и не содержится буквы других алфавитов
# ●	содержит минимум 2 цифры
# ●	в конце имени обязательно нужно указывать “login”
# примеры валидных значений
# 	n12login
# 	name22login
# 	2name2login
# и т.д.
#
# Программа должна вывести кол-во валидных значений и показать их в консоли.

# Не понял как в регулярном выражении обойти тот факт, что сочетание букв 'login' уже содержит
# "минимум 1 букву латинского алфавита", но принципиально работает - 'login' в конце тоже обязательное условие:

import re

logins = '''
n12login
name22login
2name2login
2namelogin2
1ывмыв312login
МЦАЦМcvYRBDмавzzzывм12123login
13124124124login
13124124124LoGiN
123alogi
12golni
golni12
12login
login12
login
111login
111
!@#!@#$!$%!login
login2vfvs
LOGIN231vsdfsdfg
fsf1LOGIN
'''
logins_list = list(logins.split())
r = re.compile(r'^(?=[a-zA-Z]*?\d[a-zA-Z]*\d)(?=.*[a-zA-Z]).+login\b$')
newlist = list(filter(r.match, logins_list))
print("Валидные значения:")
i = 0
for match in newlist:
    i += 1
    print(f"{i}: {match}")
print(f"Количество валидных значений всего: {i}")

# + я так и не понял почему, но если я использую функцию findall (как в предыдущих заданиях и на лекции)
# программа вообще не ищет совпадений - код для примера ниже (прошу не учитывать его при оценке ;)))
#

# import re
#
# logins = '''
# n12login
# name22login
# 2name2login
# 2namelogin2
# 1ывмыв312login
# 13124124124login
# 13124124124LoGiN
# 123alogi
# 12golni
# golni12
# 12login
# login12
# login
# 111login
# 111
# !@#!@#$!$%!login
# login2vfvs
# LOGIN231vsdfsdfg
# fsf1LOGIN
# '''
# reg_ex = r'^(?=[a-zA-Z]*?\d[a-zA-Z]*\d)(?=.*[a-zA-Z]).+login\b$'
# valid_logins = re.findall(reg_ex, logins)
# print("Валидные значения:")
# i = 0
# for match in valid_logins:
#     i += 1
#     print(f"{i}: {match}")
# print(f"Количество валидных значений всего: {i}")

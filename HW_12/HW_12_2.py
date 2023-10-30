# Посчитайте кол-во чисел в произвольной строке
# (число - это набор цифр, перед числом и после числа ставятся пробелы)

s = "54215243 n43251514 413511 14354315143j 51342541n jjkjkhjk jbjkbkjjbbj4234kj23  324j4234jkjkbjkb 23434"
numbers = s.split()
count = 0
for num in numbers:
    if num.isdigit():
        count += 1
print(f"Количество чисел в заданной строке: {count}")

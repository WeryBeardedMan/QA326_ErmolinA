# Дано трехзначное число. Найти произведение цифр.
# Пример:
# 123
# 1*2*3=6

print("Введите целое трехзначное число:")
input_num = int(input())
list_numbers = [int(i) for i in str(input_num)]
mult_result = 1
for num in list_numbers:
    mult_result *= num
print("Результат перемножения цифр в числе: ", mult_result)

# Выведите столбец чисел от start (определяется пользователем) до end, используя цикл while. Найти произведение чисел

print("Введите начало диапазона чисел:")
start = int(input())
print("Введите конец диапазона чисел:")
end = int(input())
result_of_mult = 1
while start <= end:
    print(start, end = "\n")
    result_of_mult = result_of_mult * start
    start += 1
print(f"Результат перемножения чисел в указанном диапазоне: {result_of_mult}")

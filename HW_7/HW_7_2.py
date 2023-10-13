# распечатайте все числа, которые делятся на 3 от start до end(включительно)
# (start, end - могут быть перепутаны),
# start , end- гарантируется, что целые числа

print("""Введите два целых числа, на экран будут выведены
числа кратные 3 в диапазоне от одного числа до другого.""")
start = int(input("Введите первое число:"))
end = int(input("Введите второе число:"))
if start <= end:
    for i in range(start, end+1):
        if i % 3 == 0:
            print(i)
            start += 1
else:
    for i in reversed(range(end, start+1)):
        if i % 3 == 0:
            print(i)
            end += 1

# Посчитайте кол-во букв в произвольной строке
row = input()
print("Количество букв:", sum(map(str.isalpha, row)))

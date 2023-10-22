# напечатать полый прямоугольник (заданы длина, ширина и символ) при помощи цикла for

width = int(input("Введите длину прямоугольника: "))
length = int(input("Введите ширину прямоугольника: "))
simbol = str(input("Введите символ, которым будет нарисована фигура: "))
for i in range(1, width+1):
    if i == 1 or i == width:
        print((simbol + " ") * length)
    else:
        print((simbol + " ") + "  " * (length-2) + (simbol + " "))

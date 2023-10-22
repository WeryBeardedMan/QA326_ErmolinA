# Поменять местами наибольший и наименьший элементы массива

numbers = [1, 34, 5, 6, 12, 2, 0, 11, 7]
print(f"Исходный массив: {numbers}")
i, j = [f(range(len(numbers)), key=numbers.__getitem__) for f in [min, max]]
numbers[i], numbers[j] = numbers[j], numbers[i]
print(f"В исходном массиве поменяны местами наибольший и наименьший элемент: {numbers}")

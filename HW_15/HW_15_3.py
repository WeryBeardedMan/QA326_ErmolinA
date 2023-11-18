# Дан список чисел (можно создать любым способом, но приветствуется через лямбду функцию и random).
# Необходимо создать новый список чисел, которые будут составлять 70% от исходного числа.
# Для создания такого списка использовать функцию map().
# Необходимо посчитать разницу между суммами исходного списка и преобразованного

import random
random_num_list = lambda: random.randint(1, 123)
first_num_list = []
for i in range(17):
    first_num_list.append(random_num_list())
print(f'Сформирован список: {first_num_list}')
recount_list = list(map(lambda x: x * 0.7, first_num_list))
print(f'70% от чисел исходного списка: {recount_list}')
print(f"Разница сумм списков: {sum(first_num_list) - sum(recount_list)}")  # округление не делал

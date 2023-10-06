# Написать программу для следующей задачи
# работают 3 сотрудника, у них есть оклад в размере 300.
# Если сотрудник выполнит 50 и более продаж, то получит премию в размере 30% от оклада, если более 75,
# то получит премию в размере 65% от оклада, а если 100, то - 100% от оклада
#
employee_1 = 300
employee_2 = 300
employee_3 = 300
print("Для какого сотрудника будем рассчитывать премию? Введите 1, 2, или 3:")
choice_employee = int(input())
print("Введите количество продаж, которые выполнил сотрудник (целое число):")
sales = int(input())
if 1 <= choice_employee <= 3 and sales >= 0:
    if choice_employee == 1 and sales < 50:
        print("Сотрудник 1 не получит премию")
    elif choice_employee == 1 and 50 <= sales <= 75:
        sales = employee_1 * 30/100
        print(f"Сотрудник 1 получит премию в размере: {sales}")
    elif choice_employee == 1 and 75 < sales < 100:
        sales = employee_1 * 65/100
        print(f"Сотрудник 1 получит премию в размере: {sales}")
    elif choice_employee == 1 and sales >= 100:
        sales = employee_1
        print(f"Сотрудник 1 получит премию в размере: {sales}")
    if choice_employee == 2 and sales < 50:
        print("Сотрудник 2 не получит премию")
    elif choice_employee == 2 and 50 <= sales <= 75:
        sales = employee_1 * 30/100
        print(f"Сотрудник 2 получит премию в размере: {sales}")
    elif choice_employee == 2 and 75 < sales < 100:
        sales = employee_1 * 65/100
        print(f"Сотрудник 2 получит премию в размере: {sales}")
    elif choice_employee == 2 and sales >= 100:
        sales = employee_1
        print(f"Сотрудник 2 получит премию в размере: {sales}")
    if choice_employee == 3 and sales < 50:
        print("Сотрудник 3 не получит премию")
    elif choice_employee == 3 and 50 <= sales <= 75:
        sales = employee_1 * 30/100
        print(f"Сотрудник 3 получит премию в размере: {sales}")
    elif choice_employee == 3 and 75 < sales < 100:
        sales = employee_1 * 65/100
        print(f"Сотрудник 3 получит премию в размере: {sales}")
    elif choice_employee == 3 and sales >= 100:
        sales = employee_1
        print(f"Сотрудник 3 получит премию в размере: {sales}")
else:
    print("Введены не существующие сотрудники или неверное количество продаж, перечитайте условия ввода.")

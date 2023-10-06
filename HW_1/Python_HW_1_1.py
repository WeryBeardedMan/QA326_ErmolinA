# Пользователь вводит сумму вклада в банк и годовой процент. Найдите сумму вклада через 5 лет
#
print("Введите сумму вклада:")
deposit_amount = float(input())
print("Введите готовой процент по вкладу:")
annual_percentage = float(input())
print("Введите срок вклада кратно 1 году:")
number_of_years = int(input())
year = 0
while year < number_of_years:
    annual_income = (deposit_amount * (1 + (annual_percentage / 100))) - deposit_amount
    deposit_amount += annual_income
    year += 1
print("Сумма вклада за указанный период составит:", deposit_amount)

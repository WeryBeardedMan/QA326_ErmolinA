# Дан день, месяц и год (может быть любым, даже отрицательным)
# Определить существует ли дата?
#
print("Введите год:")
year = int(input())
print("Введите месяц:")
mounth = int(input())
print("Введите день:")
day = int(input())
if 0 < mounth < 13 and 0 < day < 32:
    if mounth == 1:
        print("Такая дата существует")
    elif mounth == 3:
        print("Такая дата существует")
    elif mounth == 4:
        if day < 31:
            print("Такая дата существует")
        else:
            print("Такой даты не существует")
    elif mounth == 5:
        print("Такая дата существует")
    elif mounth == 6 and 0 < day < 31:
        if day < 31:
            print("Такая дата существует")
        else:
            print("Такой даты не существует")
    elif mounth == 7:
        print("Такая дата существует")
    elif mounth == 8:
        print("Такая дата существует")
    elif mounth == 9 and 0 < day < 31:
        if day < 31:
            print("Такая дата существует")
        else:
            print("Такой даты не существует")
    elif mounth == 10:
        print("Такая дата существует")
    elif mounth == 11 and 0 < day < 31:
        if day < 31:
            print("Такая дата существует")
        else:
            print("Такой даты не существует")
    elif mounth == 12:
        print("Такая дата существует")
    elif mounth == 2 and day > 29:
        print("Такой даты не существует")
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if mounth == 2:
            if day < 30:
                print("Такая дата существует")
    else:
        if mounth == 2:
            if day < 29:
                print("Такая дата существует")
            else:
                print("Такой даты не существует")
else:
    print("Такой даты не существует")

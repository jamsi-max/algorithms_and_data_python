# Задание № 8
# Определить, является ли год, который ввел пользователь, високосным или не високосным


y = int(input("Введите год: "))
if (y % 4) == 0:
    if (y % 100) == 0:
        if (y % 400) == 0:
            print(f'Введёный вами год - {y} является високосным')
        else:
            print(f'Введёный вами год - {y} не високосный')
    else:
        print(f'Введёный вами год - {y} является високосным')
else:
    print(f'Введёный вами год - {y} не високосный')
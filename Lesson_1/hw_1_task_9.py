# Задание № 9
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

print("Определение среднего из чисел")
a = int(input("Ведите первое число: "))
b = int(input("Ведите второе число: "))
c = int(input("Ведите третье число: "))

if a > b and a < c:
    print(f'Средним числом является {a}')
elif b > a and b < c:
    print(f'Средним числом является {b}')
else:
    print(f'Средним числом является {c}')
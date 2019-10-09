# Задание №9
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр

def sum(a):
    if not a:
        return a
    return (a%10)+sum(a // 10)

itter, val, val_sum = 1, 0, 0

while itter:
    itter = int(input('Введите натуральное число: '))
    if sum(itter) > val_sum:
        val_sum, val = sum(itter), itter
print(f'Наибольшая сумма цифр {val_sum} у числа {val}.')

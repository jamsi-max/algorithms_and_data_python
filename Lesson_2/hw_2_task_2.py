# Задача № 2
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

x=0 # чётные
y=0 # нечётные
a = int(input('Введите число: '))

while a:
    if (a % 2):
        y+=1
    else:
        x+=1
    a//=10

print(f'{x} - четных, {y} - нечётных')

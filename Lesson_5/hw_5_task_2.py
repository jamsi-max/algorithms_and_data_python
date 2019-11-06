# Задание № 2
# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

key = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

# функция перевода в десячичное число
def ch_dec(num):
    res = 0
    num.reverse()
    for i, v in enumerate(num):
        res += key[v] * (16 ** i)
    return res

# функция перевода в 16-ое число
def ch_hex(num):
    res = deque()
    total = ''
    while num:
        res.append(num%16)
        num = num // 16
    res.reverse()

    for x in res:
        for k, v in key.items():
            if v == x:
                total += k
    return total

while True:
    opr = input('Выберите операцию: 1 - сложение, 2 - умножение (0- Выход): ')
    if opr == '1':
        a_hex = deque(input('Введите 1 число:').upper())
        b_hex = deque((input('Введите 2 число: ')).upper())
        print('Сумма чисел равна: ', (ch_hex(ch_dec(a_hex) + ch_dec(b_hex))))
    elif opr == '2':
        a_hex = deque(input('Введите 1 число:').upper())
        b_hex = deque((input('Введите 2 число: ')).upper())
        print((ch_hex(ch_dec(a_hex) * ch_dec(b_hex))))
    elif opr == '0':
        break
    else:
        print('Некорректный ввод')
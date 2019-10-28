# Успел таки реализовать рекурсию с мемоизацией очень инетересно Ваше мнение! Правильно ли яеё понял и правильна
# ли реализация!!!

import random
import sys
from collections import deque

# Функция подсчёта размера
def show_size(x):
    res=[]
    def run(elm):
        res.append(sys.getsizeof(elm))
        if hasattr(elm, '__iter__'):
            if hasattr(elm, 'items'):
                for key, value in elm.items():
                    run(key)
                    run(value)

            elif not isinstance(elm, str):
                for item in elm:
                    run(item)
    for i in x:
        run(i)
    return sum(res)

#************************************************************************
# Выбрал задачу где меняются местами меньший и больший элементы
# Вариант № 1. Используем список
def fun_1():
    SIZE = 10
    MAX_ITEM = 100
    MIN_ITEM = 0
    ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(ls)

    num_max = ls[0]
    num_min = ls[0]

    for i in ls:
        if i > num_max:
            num_max = i
        if i < num_min:
            num_min = i

    for pos_spam, spam in enumerate(ls):
        if spam == num_max:
            ls[pos_spam] = num_min
        if spam == num_min:
            ls[pos_spam] = num_max

    print(ls)

# Счтитаем размер
    print('=' * 80)
    print(f'Размер - {show_size(vars().values())}b')
    print('=' * 80)

# Вариант №2. Используем кортеж
def fun_2():
    ls = (11, 18, 48, 1, 99, 67, 43, 77, 0, 4)
    print(ls)

    num_max = ls[0]
    num_min = ls[0]
    _ls = []
    for i in ls:
        if i > num_max:
            num_max = i
        if i < num_min:
            num_min = i

    for pos_spam, spam in enumerate(ls):
        _ls.append(spam)
        if spam == num_max:
            _ls[pos_spam] = num_min
        if spam == num_min:
            _ls[pos_spam] = num_max

    print(_ls)

# Счтитаем размер
    print('=' * 80)
    print(f'Размер - {show_size(vars().values())}b')
    print('=' * 80)

# Вариант № 3. Используем очередь
def fun_3():
    SIZE = 10
    MAX_ITEM = 100
    MIN_ITEM = 0
    ls = deque(random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE))
    print(ls)

    num_max = ls[0]
    num_min = ls[0]

    for i in ls:
        if i > num_max:
            num_max = i
        if i < num_min:
            num_min = i

    for pos_spam, spam in enumerate(ls):
        if spam == num_max:
            ls[pos_spam] = num_min
        if spam == num_min:
            ls[pos_spam] = num_max

    print(ls)

# Счтитаем размер
    print('=' * 80)
    print(f'Размер - {show_size(vars().values())}b')
    print('=' * 80)

# Вариант из лекции
def fun_4():
    N = 10
    MIN_ITEM = -800
    MAX_ITEM = -750
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)]
    print(array)

    idx_min = 0
    idx_max = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    print(array)

# Счтитаем размер
    print('=' * 80)
    print(f'Размер - {show_size(vars().values())}b')
    print('=' * 80)


fun_1()
fun_2()
fun_3()
fun_4()

# *********************************************************************************************
# Вспомнил про ещё одну задачу, где у меня была ошибка. Точнее Вы указали, что конкатенация не лучшее решение
# и я его исправил в ДЗ. Но тут вдруг стало интересно и протестировать оба варианта. Вывод в самом низу.

# Вариант № 1 Без конкатенации(исправленный)
def f_1():
    num = int(input('Сколько чисел вы хотите ввести: '))
    find_num = input('Какую цифру от 0 до 9 будем искать: ')

    count, step = 0, 1

    while step <= num:
        a = int(input(f'Введите число №{step}: '))
        for i in str(a):
            if i == find_num:
                count += 1
        step += 1

    print(f'Цифра {find_num} встречается в введёных числах {count} раз!')

    # Счтитаем размер
    print('=' * 80)
    print(f'Размер - {show_size(vars().values())}b')
    print('=' * 80)

# Вариант № 2 С конкатенацией(неудачное решение ДЗ)
def f_2():
    num = int(input('Сколько чисел вы хотите ввести: '))
    find_num = int(input('Какую цифру от 0 до 9 будем искать: '))

    result, count, step = '', 0, 1
    PASS = 0

    while step <= num:
        result = result + input(f'введите число №{step}: ')
        step += 1

    for i in result:
        count += 1 if int(i) == find_num else PASS

    print(f'Цифра {find_num} встречается в введёных числах {count} раз!')

    print(vars().values())
    # Счтитаем размер
    print('=' * 80)
    print(f'Размер - {show_size(vars().values())}b')
    print('=' * 80)

f_1()
f_2()

# ******************************************************************************************************
# ВЫВОД:
# И так результаты следующие: в задаче где местами меняются мин и макс числа при использовании списка(массива)
# размер получился минимальный, однако самый минимальны размер былв варианте из лекции так как там на один цикл
# меньше и соответсвенно на одну переменную меньше. Далее при использовании кортежа и очереди размер возрастает
# в случае с кортежем все таки виноват создаваемый список.
# Вывод по задаче с поиском цифры в ведёных числах. Разница в размере примерно 50b при этом сстарый список не
# считается и не отображается, получается функции locals globals dir не видят старый вариант и отображают только
# один вновь полученный.
# В целом достаточно любопытные результаты! К сожалению из-за нехватки времени не удалось реализовать просто вызовом
# функции тут прям напрашивается рекурсия с меморизацией но времени к сожалению катастрофически не хватает.
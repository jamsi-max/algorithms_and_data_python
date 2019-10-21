# Задание № 1
import timeit
import cProfile

arr = [46, 9, -50, -3, 22, -2, -49, 18, 2, 44, -13, -7, 25, -31, 2, 28, -11, 49, 16, 11]
print(arr)

# Вариант №1 мой из ДЗ №3. Логика: находим в цикле минимальное число из массива и запоминаем его и его позицию
# далее ищем опять минимальное число у которого индекс не равен индексу первого минимального.
# Используем: for, for, enumerate
def fun_1(array):
    item_first = array[0]
    first_pos = 0
    item_last = array[0]
    for pos, item in enumerate(array):
        if item < item_first:
            item_first = item
            first_pos = pos
    for pos, item in enumerate(array):
        if item < item_last and first_pos != pos:
            item_last = item
    return item_first, item_last

cProfile.run('fun_1(arr)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 hw_4_task_1_1.py:14(fun_1)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

min_first, min_second = fun_1(arr)
print(f'Два наименьших числа в массиве {min_first} и {min_second}')

s = """
arr = [46, 9, -50, -3, 22, -2, -49, 18, 2, 44, -13, -7, 25, -31, 2, 28, -11, 49, 16, 11]
def fun_1(array):
    item_first = array[0]
    first_pos = 0
    item_last = array[0]
    for pos, item in enumerate(array):
        if item < item_first:
            item_first = item
            first_pos = pos
    for pos, item in enumerate(array):
        if item < item_last and first_pos != pos:
            item_last = item
    return item_first, item_last

fun_1(arr)
"""
print(timeit.timeit(s, number=1000))
# 0.024396702999999992   - 10 элементов
# 0.06924812300000001    - 100 элементов
# 0.435812458            - 1000 элементов
# 3.4528304530000002     - 10 000 элементов   /3.366346324
# 33.196695956           - 100 000 элементов


# Вариант № 2. Логика: сортируем массив от меньшего к большему и выводим первых два числа массива. Используем два
# Используем: while, for, append, pop
def fun_2(arr):
    _arr = []
    while arr:
        spam = 0
        for x, y in enumerate(arr):
            if y < arr[spam]:
                spam = x
        _arr.append(arr.pop(spam))
    return _arr[0], _arr[1]

cProfile.run('fun_2(arr)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.089    0.089 <string>:1(<module>)
#        1    0.088    0.088    0.089    0.089 hw_4_task_1_2.py:13(fun_2)
#        1    0.000    0.000    0.089    0.089 {built-in method builtins.exec}
#     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1000    0.001    0.000    0.001    0.000 {method 'pop' of 'list' objects}

min_first, min_second = fun_2(arr)
print(f'Два наименьших числа в массиве {min_first} и {min_second}')

s="""
arr = [46, 9, -50, -3, 22, -2, -49, 18, 2, 44, -13, -7, 25, -31, 2, 28, -11, 49, 16, 11]
def fun_2(arr):
    _arr = []
    while arr:
        spam = 0
        for x, y in enumerate(arr):
            if y < arr[spam]:
                spam = x
        _arr.append(arr.pop(spam))
    return _arr[0], _arr[1]

fun_2(arr)
"""
print(timeit.timeit(s, number=1000))
# 0.030110848999999995  - 10 элемнтов
# 0.194273503           - 100 элемнтов
# 9.183067899           - 1000 элемнтов       /9.009173324999999

# Вариант №3. Логика: находим минимальное число выкалываем его из массива далее находим следующее минимальное число.
# Используем: for, for, enumerate, pop
arr = [46, 9, -50, -3, 22, -2, -49, 18, 2, 44, -13, -7, 25, -31, 2, 28, -11, 49, 16, 11]
def fun_3(arr):
    spam = 0
    for x, y in enumerate(arr):
        if y < arr[spam]:
            spam = x
    first = arr[spam]
    arr.pop(spam)

    spam = 0
    for x, y in enumerate(arr):
        if y < arr[spam]:
            spam = x
    second = arr[spam]
    return first, second

cProfile.run('fun_3(arr)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 hw_4_task_1_3.py:13(fun_3)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}

min_first, min_second = fun_3(arr)
print(f'Два наименьших числа в массиве {min_first} и {min_second}')

s = """
arr = [46, 9, -50, -3, 22, -2, -49, 18, 2, 44, -13, -7, 25, -31, 2, 28, -11, 49, 16, 11]
def fun_3(arr):
    spam = 0
    for x, y in enumerate(arr):
        if y < arr[spam]:
            spam = x
    first = arr[spam]
    arr.pop(spam)

    spam = 0
    for x, y in enumerate(arr):
        if y < arr[spam]:
            spam = x
    second = arr[spam]
    return first, second

fun_3(arr)
"""
print(timeit.timeit(s, number=1000))
# 0.025308982999999993    - 10 элемнетов
# 0.061644854             - 100 элемнетов
# 0.44168192599999995     - 1000 элемнетов
# 3.573676189             - 10 000 элемнетов   /3.6628288529999997
# 34.200295485            - 100 000 элементов


# Вариант №4. Из лекции для сравнения
arr = [46, 9, -50, -3, 22, -2, -49, 18, 2, 44, -13, -7, 25, -31, 2, 28, -11, 49, 16, 11]
def fun_4(array):
    min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)

    for i in range(2, len(array)):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam

        elif array[i] < array[min_second]:
            min_second = i
    return arr[min_first], arr[min_second]

cProfile.run('fun_4(arr)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 hw_4_task_1_4.py:12(fun_4)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

min_first, min_second = fun_4(arr)
print(f'Два наименьших числа в массиве {min_first} и {min_second}')

s = """
arr = [46, 9, -50, -3, 22, -2, -49, 18, 2, 44, -13, -7, 25, -31, 2, 28, -11, 49, 16, 11]
def fun_4(array):
    min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)

    for i in range(2, len(array)):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam

        elif array[i] < array[min_second]:
            min_second = i
    return arr[min_first], arr[min_second]

fun_4(arr)  
"""
print(timeit.timeit(s, number=1000))
# 0.036665228999999994    - 10 элементов
# 0.061999474             - 100 элементов
# 0.41673785599999996     - 1000 элементов
# 3.74377755              - 10 000 элементов   /3.493569597
# 34.588117344            - 100 000 элементов

#--------------------------------------------------------------------------------------------------------------
# Вывод: Наиболее оптимальный алгоритм имеент вариант 1 и 3. В месте с тем, неожиданно вариант номер 3, где используется, по мимо
# двух циклов ещё и функция 'pop' которая по своей логики должна при удалении элемента из масива сдвигать остатвшиеся в лево,
# по сути весь массив данных(если елемент не последний), работает даже на тысячные секунды быстрее варианта из лекции, где
# используется всего один цикл. Данные подтверждаются и результатами утилиты cProfile. Так, отчетливо видно при её использовании,
# что вариант номер 2 например за время своей работы вызывает два метода по 1000 раз кажды, что соответственно и сказывается
# на медленной работе алгоритма, а вот алгоритм 1 вызывает всего четыре функции против пяти у 3 и 4 варианта, что и определяет
# по сути его незначительный перевес в быстродействии в сравнении с остальными.
# Все замеры  на cProfile и timeit проводил с использованием рандомного наполнения исходного массива с числом выбора
# элементов от -100 до 100 и длинной массива 10, 100, 1000, 10 000, 100 000 в каждом варианте индивидуально до того значения
# пока компьютер не засыпал. Также из кода были убраны все функции print.


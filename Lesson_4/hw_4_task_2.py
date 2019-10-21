# Задание №2
# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов

import timeit
import cProfile

# Вариант № 1 Решето Эратосфена
def sieve(num):
    res = []
    START = 5
    while len(res) < num:
        arr = [i for i in range(START+1)]
        arr[1] = 0
        for i in range(2, len(arr)):
            if arr[i] != 0:
                j = i + i
                while j <= START:
                    arr[j] = 0
                    j += i
        for i in arr:
            if i != 0 and i not in res:
                res.append(arr[i])
        START += 1
    return res[num-1]

#cProfile.run('sieve(100)')
# #         1716 function calls in 0.141 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.141    0.141 <string>:1(<module>)
#       537    0.015    0.000    0.015    0.000 hw_4_task_2.py:13(<listcomp>)
#         1    0.126    0.126    0.141    0.141 hw_4_task_2.py:9(sieve)
#         1    0.000    0.000    0.141    0.141 {built-in method builtins.exec}
#      1075    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
s = """
def sieve(num):
    res = []
    START = 5
    while len(res) < num:
        arr = [i for i in range(START+1)]
        arr[1] = 0
        for i in range(2, len(arr)):
            if arr[i] != 0:
                j = i + i
                while j <= START:
                    arr[j] = 0
                    j += i
        for i in arr:
            if i != 0 and i not in res:
                res.append(arr[i])
        START += 1
    return res[num-1]
sieve(80)
"""
#print(timeit.timeit(s, number=100))
# 0.0050937960000000115   - 5 простое число
# 0.034606751000000005    - 10 простое число
# 0.17359141700000003     - 20 простое число
# 1.1028359269999999      - 40 просто число
# 9.647940446             - 80 простое число

# Вариант № 2 Алгорит деления без остатка
def no_sieve(num):
    res = []
    START = 5
    while len(res) < num:
        arr = [i for i in range(2,START+1)]
        for x in arr:
            frequency = 0
            for y in range(2, x+1):
                if x % y == 0:
                    frequency += 1
            if frequency == 1 and x not in res:
                res.append(x)
        START += 1
    return res[num-1]

#cProfile.run('no_sieve(100)')
#         1179 function calls in 3.746 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    3.746    3.746 <string>:1(<module>)
#         1    3.723    3.723    3.746    3.746 hw_4_task_2.py:30(no_sieve)
#       537    0.023    0.000    0.023    0.000 hw_4_task_2.py:34(<listcomp>)
#         1    0.000    0.000    3.746    3.746 {built-in method builtins.exec}
#       538    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

s = """
def no_sieve(num):
    res = []
    START = 5
    while len(res) < num:
        arr = [i for i in range(2,START+1)]
        for x in arr:
            frequency = 0
            for y in range(2, x+1):
                if x % y == 0:
                    frequency += 1
            if frequency == 1 and x not in res:
                res.append(x)
        START += 1
    return res[num-1]
no_sieve(80)
"""
print(timeit.timeit(s, number=100))
# 0.009646774999999996    - 5
# 0.155631199             - 10
# 1.0574380749999999      - 20
# 12.683987196            - 40
# 169.630048534           - 80

# Вывод. Достаточно интересные результаты. Явно решето Эратосфена выигрывает несмотря на несовсем граммотно
# адаптированный мной алгоритм. Но тем не менее результат разница ощутимо. При обычном делении без остатка скорость
# значительно падает. При этом, что интересно, число вызова функций у Эратосфена больше почти на 500. Данный пример
# очень характерно показал, посравнению с первой задачей, что оценка скорости работы алгоритмов должна осуществлятся
# по нескольким критериям.
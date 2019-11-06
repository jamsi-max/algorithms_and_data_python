# Задание № 4
# Определить, какое число в массиве встречается чаще всего

import random
# Вариант № 1. Одно чаще всего встречающееся число в массиве

SIZE = 10
MAX_ITEM = 20
MIN_ITEM = 10
ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ls)

elm = 0
count = 0

for first in ls:
    spam = 0
    for last in ls:
        if first == last:
            spam += 1
    if spam > count:
        count = spam
        elm = first

print(f'Чаще всего в массиве встречается {elm} - {count} раза')

# Вариант № 2 Если числел несколько и они одинаково часто встречаются. Использовал словарь вроде не запрещалось
SIZE = 15
MAX_ITEM = 10
MIN_ITEM = 0
ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ls)

elm_repeat = {}      # словарь состоящий из чисел и количества их повторей
max_count = 0        # максимальное число повторений
total_elm=[]         # список чисел чаще всего встречающихся в массиве

for i in ls:
    spam = 0
    for x in ls:
        if i == x:
            spam +=1
    elm_repeat[i] = spam
    if spam > max_count:
         max_count = spam

for x, y in elm_repeat.items():
    if y == max_count:
        total_elm.append(x)

print(f'Чаще всего в массиве встречается {total_elm} - {max_count} раза')
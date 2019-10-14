# Задание № 6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MAX_ITEM = 10
MIN_ITEM = 0
ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ls)

max_num = ls[0]
max_pos = 0
min_num = ls[0]
min_pos = 0
ls_sum = 0

for pos_spam, spam in enumerate(ls):
    if spam > max_num:
        max_num = spam
        max_pos = pos_spam
    elif spam < min_num:
        min_num = spam
        min_pos = pos_spam

if max_pos > min_pos:
    for i in range(min_pos+1,max_pos):
        ls_sum += ls[i]
else:
    for i in range(max_pos+1, min_pos):
        ls_sum +=ls[i]
print(f'Сумма между мининмальны элементом {min_num} и максимальным элементом {max_num} в массиве равна {ls_sum}')

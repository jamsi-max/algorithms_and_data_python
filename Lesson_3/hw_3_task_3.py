# Задание № 3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

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

# Задание №2
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения

import random

SIZE = 10
MAX_ITEM = 10
MIN_ITEM = -10
ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ls)

elm = ls[0]
pos = 0

for i in ls:
    if i < elm:
        elm = i

for pos_spam, spam in enumerate(ls):
    if elm < spam < 0:
        elm = spam
        pos = pos_spam

print(f'Максимальный отрицательный элемент равен {elm} находится в массиве на {pos} месте.')

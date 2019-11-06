# Задание № 7
# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
# собой (оба являться минимальными), так и различаться
import random

SIZE = 10
MAX_ITEM = 10
MIN_ITEM = 0
ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ls)

item_first = ls[0]
first_pos = 0
item_last = ls[0]
last_pos = 0

for pos, item in enumerate(ls):
    if item < item_first:
        item_first = item
        first_pos = pos

for pos, item in enumerate(ls):
    if item < item_last and first_pos != pos:
        item_last = item

print(f'Два наименьших числа в массиве {item_first} и {item_last}')
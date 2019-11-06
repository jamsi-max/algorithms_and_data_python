#Задание № 2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# Решил немного по своей логиге. Сначала нужно разбить массив делением примерно пополам до одного элементных и
# начинать сравнивать и сливать постепенно. Поэтому просто исходный массив путем перебора сделал масивом из
# одноэлементных массивов. Не знаю насколько это правильно но по ресурсозатратам должно выйграть у рекурсии вроде.
import random

array=[]
LENGTH = 15
# Генерируем массив в промежутке от 0 включая до 50 не включая
while len(array) != LENGTH:
    a = random.uniform(0,50)
    if a != 50:
        array.append(a)

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    print(arr)
    global array

    def run(arr_1, arr_2):
        buf = []
        while len(arr_2) and len(arr_1):
            if arr_1[0] > arr_2[0]:
                buf.append(arr_2.pop(0))
            else:
                buf.append(arr_1.pop(0))
        buf.extend(arr_1) if arr_1 else buf.extend(arr_2)
        return buf
    # Вместо деления массива до 1-го элемента сделал перевод всех элементов в одноэлементные массивы
    for i in range(len(arr)):
        arr.append([arr.pop(0)])

    while len(arr) > 1:
        arr.append(run(arr.pop(0), arr.pop(0)))
    array = arr[0]


merge_sort(array)
print(array)



# Задание №3
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте
# метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима)
import random

# Варинат № 1. Без сортировки. Решал методом от противного. Каждый елемент проверяется по порядку является ли он
# медианой, то есть считаем есть ли справа от него элементы, которые не меньше медианы и соответственно слева не больше.
m = int(input('Введите число m: '))
array = [random.randint(0,10) for _ in range(2*m+1)]

print(array)

def mediana(arr):
    pos = len(array)//2 # позиция медианы
    for i in range(len(array)):
        left = 0
        right = 0
        for j in range(len(array)):
            if array[i] >= array[j] and left != pos:
                left += 1
            if array[i] <= array[j] and right !=pos:
                right += 1
            if left == right == pos:
                print(f'Медиана равна {array[i]}')
                break
        if left == right == pos:
            break

mediana(array)

# Эта строчка исключительно для проверки правильности результата. Сортируем и смотрим что есть медиана. Хотел своим
# способом сортироват так можно было и на второй вопрос задачи ответить, убить двух зайце, но к моему сожалению просто
# не хватило времени. Для себя сегодня же вечером доделаю)
array.sort()
print(array)

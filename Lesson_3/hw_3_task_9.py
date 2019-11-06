# Задание № 9
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

LINE = 5
COLUMN = 4

matrix = [[random.randint(-10,10) for x in range(COLUMN)] for y in range(LINE)]

print(*matrix, sep='\n')
print('*'*90)

column_result=[]

for column in range(0, COLUMN):
    spam = matrix[0][column]
    for line in range(0,LINE):
        if matrix[line][column] < spam:
             spam = matrix[line][column]
    column_result.append(spam)

max_number = column_result[0]
for item in column_result:
    if item > max_number:
        max_number =item
print(f'Максимальный элемент среди минимальных элементов {column_result} столбцов матрицы равен {max_number}')

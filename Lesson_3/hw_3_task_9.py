# Задание № 9
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

LINE = 4
COLUMN = 5

matrix = [[random.randint(-10,10) for x in range(LINE)] for y in range(COLUMN)]

print(*matrix, sep='\n')
print('*'*90)

column_result=[]

for line in range(0, LINE):
    spam = matrix[0][line]
    for column in range(0,COLUMN):
        if matrix[column][line] < spam:
             spam = matrix[column][line]
    column_result.append(spam)

max_number = column_result[0]
for item in column_result:
    if item > max_number:
        max_number =item
print(f'Максимальный элемент среди минимальных элементов {column_result} столбцов матрицы равен {max_number}')

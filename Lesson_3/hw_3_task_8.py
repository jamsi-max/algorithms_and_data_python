# Задание № 8
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести
# полученную матрицу

LINE = 4
COLUMN = 4

matrix = [[int(input(f'Введите в столбце № {y+1} число № {x+1}: ')) for x in range(LINE)] for y in range(COLUMN)]

print('*'*10,'MATRIX','*'*10)
for column in matrix:
    spam = 0
    for line in column:
        spam += line
        print(f'{line:>5}', end = '')
    print(f'{spam:>5}')
print('*'*28)

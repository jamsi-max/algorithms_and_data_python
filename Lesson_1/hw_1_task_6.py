# Задание № 6
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Введите номер буквы в алфавите от 1 до 26: '))
print(chr(97 + num - 1))

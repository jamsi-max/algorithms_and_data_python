# Задача №1
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9

ls_long = [i for i in range(2, 99)]
ls_smal = [2, 3, 4, 5, 6, 7, 8, 9]
for x in ls_smal:
    count = 0
    for b in ls_long:
        if not b%x:
            count += 1
    print(f'числу {x} из массива кратны {count} чисел')


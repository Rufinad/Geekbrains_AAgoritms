print('пятое задание')
import random
''' В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве'''
# постановка задачи
SIZE_M = 10
MIN_ITEM = -10
MAX_ITEM = 10
massive = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)]
print(massive)

# решение задачи

sub_zero = []

for item in massive:
    if item < 0:
        sub_zero.append(item)

try:
    min_max = sub_zero[0]
    for item in sub_zero:
        if item > min_max:
            min_max = item
    print(f'максимальное отрицательное число в массиве исеет индекс {massive.index(min_max)}')
except IndexError:
    print('В массиве нет отрицательных чисел')
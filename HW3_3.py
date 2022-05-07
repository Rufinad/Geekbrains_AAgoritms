print('третье задание')
'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы'''
# постановка задачи

import random

SIZE_M = 10
MIN_ITEM = 0
MAX_ITEM = 100
massive = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)]
print(massive)

# решение задачи

min_val = massive[0]
max_val = massive[0]

# находим минимальный и максимальный элемент
for item in massive:
    if item > max_val:
        max_val = item
    if item < min_val:
        min_val = item

print(min_val, max_val)

# меняем местами максимальное значение с минимальным

massive[massive.index(min_val)] = max_val
massive[massive.index(max_val)] = min_val
print(massive)


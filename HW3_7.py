print('седьмое задание')

''' В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.'''

import random

# постановка задачи
SIZE_M = 10
MIN_ITEM = -10
MAX_ITEM = 10
massive = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)]

print(massive)

# решение задачи

# определим что first_min будет являться наименьшим значением массива
first_min = massive[0]
second_min = massive[1]
if first_min > second_min:
    first_min, second_min = second_min, first_min

# находим 2 наименьших числа массива
for i in range(2, len(massive)):
    if massive[i] < first_min:
        second_min = first_min  # чтобы не потерять преднаименьшее число
        first_min = massive[i]
    elif massive[i] < second_min:
        second_min = massive[i]

print(f'два наименьших элемента в массиве = {first_min, second_min}')
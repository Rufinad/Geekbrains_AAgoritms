print('второе задание')

'''Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.'''

# постановка задачи

import random

SIZE_M = 10
MIN_ITEM = -100000
MAX_ITEM = 100000
massive = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)]
print(massive)

# решение задачи

answer = []

for i, item in enumerate(massive):
    if item % 2 == 0:
        answer.append(i)

print(answer)


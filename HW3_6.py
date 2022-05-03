print("шестое задание")

'''В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.'''
import random
# постановка задачи
SIZE_M = 10
MIN_ITEM = -10
MAX_ITEM = 10
massive = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)]

print(massive)

# решение задачи
# находим максимальное и минимальное значение массива:

max_massive = massive[0]
min_massive = massive[0]

for item in massive:
    if item > max_massive:
        max_massive = item
    elif item < min_massive:
        min_massive = item

print(f'максимальное число в массиве = {max_massive}, минимальное {min_massive}')

# находим сумму элементов между значениями

sum_value = 0

if massive.index(min_massive) < massive.index(max_massive):
    for i in range(massive.index(min_massive)+1, massive.index(max_massive)):
        sum_value += massive[i]
    print(f'Сумма значений элементов находящихся между минимальным и максимальным элементами = {sum_value}')
elif massive.index(min_massive) > massive.index(max_massive):
    for i in range(massive.index(max_massive)+1, massive.index(min_massive)):
        sum_value += massive[i]
    print(f'Сумма значений элементов находящихся между минимальным и максимальным элементами = {sum_value}')
else:
    print(f'Сумма значений элементов находящихся между минимальным и максимальным элементами = 0')
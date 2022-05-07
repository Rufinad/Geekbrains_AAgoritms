print('четвертое задание')

'''Определить, какое число в массиве встречается чаще всего.'''

import random

SIZE_M = 10
MIN_ITEM = 0
MAX_ITEM = 10
massive = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)]
print(massive)

# решение задачи
max_count = 1
max_count_val = massive[0]
for i in range(len(massive)):
    count_i = 1
    for j in range(i+1, len(massive)):
        if massive[i] == massive[j]:
            count_i += 1
            if max_count < count_i:
                max_count = count_i
                max_count_val = massive[i]

print(f'число {max_count_val} встречается в массиве чаще всего ({max_count} раз(а))')
print('первое задание')
'''Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.'''

import random, timeit, cProfile
# постановка задачи
SIZE_M = 1000_0000
MIN_ITEM = -10
MAX_ITEM = 10
massive = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)]

# print(massive)

# решение задачи HW3_7
# 1 способ

def first_way(massive: list):
    first_min = massive[0]
    second_min = massive[1]
    if first_min > second_min:
        first_min, second_min = second_min, first_min
    for i in range(2, len(massive)):
        if massive[i] < first_min:
            second_min = first_min  # чтобы не потерять преднаименьшее число
            first_min = massive[i]
        elif massive[i] < second_min:
            second_min = massive[i]
    return first_min, second_min

print(first_way(massive))

# 2 способ
def second_way(massive: list):
    first_min = min(massive)
    new_massive = massive.copy()
    new_massive.pop(new_massive.index(first_min))
    second_min = min(new_massive)
    return first_min, second_min

print(second_way(massive))

# 3 способ
def third_way(massive: list):
    massive.sort()
    return massive[0], massive[1]

print(third_way(massive))



# print(timeit.timeit('first_way(massive)', number=1000, globals=globals()))     # SIZE=10     0.001065499999999997
# print(timeit.timeit('first_way(massive)', number=1000, globals=globals()))  # SIZE=100     0.007049799999999995
# print(timeit.timeit('first_way(massive)', number=1000, globals=globals()))  # SIZE=1000    0.0736589
# print(timeit.timeit('first_way(massive)', number=1000, globals=globals()))  # SIZE=10000   0.8005634
# print(timeit.timeit('first_way(massive)', number=1000, globals=globals()))  # SIZE=100000  8.0252967

# print(timeit.timeit('second_way(massive)', number=1000, globals=globals()))    # SIZE=10     0.0009730000000000016
# print(timeit.timeit('second_way(massive)', number=1000, globals=globals())) # SIZE=100     0.0035861999999999977
# print(timeit.timeit('second_way(massive)', number=1000, globals=globals())) # SIZE=1000    0.031421599999999994
# print(timeit.timeit('second_way(massive)', number=1000, globals=globals())) # SIZE=10000   0.3222722
# print(timeit.timeit('second_way(massive)', number=1000, globals=globals())) # SIZE=100000  2.521200800000001

# print(timeit.timeit('third_way(massive)', number=1000, globals=globals()))     # SIZE=10     0.00030479999999999396
# print(timeit.timeit('third_way(massive)', number=1000, globals=globals()))  # SIZE=100     0.0011092000000000046
# print(timeit.timeit('third_way(massive)', number=1000, globals=globals()))  # SIZE=1000    0.005864399999999992
# print(timeit.timeit('third_way(massive)', number=1000, globals=globals()))  # SIZE=10000   0.058392199999999894
# print(timeit.timeit('third_way(massive)', number=1000, globals=globals()))  # SIZE=100000  0.4400687999999988


cProfile.run('first_way(massive)')

'''5 function calls in 0.549 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.549    0.549 <string>:1(<module>)
        1    0.549    0.549    0.549    0.549 HW4_1.py:17(first_way)
        1    0.000    0.000    0.549    0.549 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


cProfile.run('second_way(massive)')

'''9 function calls in 0.360 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.053    0.053    0.360    0.360 <string>:1(<module>)
        1    0.000    0.000    0.306    0.306 HW4_1.py:33(second_way)
        1    0.000    0.000    0.360    0.360 {built-in method builtins.exec}
        2    0.250    0.125    0.250    0.125 {built-in method builtins.min}
        1    0.049    0.049    0.049    0.049 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
        1    0.007    0.007    0.007    0.007 {method 'pop' of 'list' objects}

'''

cProfile.run('third_way(massive)')

'''5 function calls in 0.092 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.092    0.092 <string>:1(<module>)
        1    0.000    0.000    0.092    0.092 HW4_1.py:43(third_way)
        1    0.000    0.000    0.092    0.092 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.092    0.092    0.092    0.092 {method 'sort' of 'list' objects}

'''

'''Выводы:
1. По результатам замеров с помощью timeit определена О(n). Выглядим справедливым тк по своей сути все способы 
перебирают полученный массив по каждому элементу и скорость выполнения меняется с увеличением объема массива.
2. С помощью cProfile были исследованы 3 способа нахождения 2 наименьших элементов массива. В результате исследования 
подтверждено что 1й способ использующий только циклы и условные операторы является самым медленным из трех,
циклы находящиеся внутри функции first_way выполняются довольно медленно. 2 способ  значительно быстрее
справляется с решением задачи, наибольшее время занимает функция min которая вызывается 2 раза. 3 способ является наиболее
удачным
'''
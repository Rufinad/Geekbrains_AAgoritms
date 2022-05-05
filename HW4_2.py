'''Написать два алгоритма нахождения i-го по счёту простого числа.
 Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

- Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
 Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

- Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:'''

import timeit, cProfile
# решаем без использования решета Эратосфена

# 1 способ
def prime(num_prime):
    prime_massive = []  # создаем массив в который будем заносить все простые числа
    for elem in range(2, num_prime**2):  # возьмем с запасом))
        if is_prime(elem) == True:  # проверка числа на простоту
                prime_massive.append(elem)
        if len(prime_massive) == num_prime:
            return prime_massive[-1]  # выводим последний элемент таблицы


def is_prime(n):
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

# print(prime(10_000))  # 104729

# решаем с использованием решета Эратосфена

def prime2(num_prime: int):
    if num_prime <= 4:  # определяем размер решета для поиска простых чисел в пределах 78498-го простого числа
        size = 10
    elif num_prime <= 25:
        size = 10 ** 2
    elif num_prime <= 168:
        size = 10 ** 3
    elif num_prime <= 1229:
        size = 10 ** 4
    elif num_prime <= 9592:
        size = 10 ** 5
    else: size = 10**6
    primes = []
    sieve = [x for x in range(2, size + 1)]  # генерируем массив

    while len(primes) != num_prime:
        # выводим новый список по принципу решета Эратосфена пока размер не достигнет введенного значения
        n = sieve[0]
        sieve = [x for x in sieve if x % n != 0]  # каждый раз убираем 0 элемент и кратные ему числа
        primes.append(n)

    return primes[num_prime-1]

# print(prime2(10000))


# print(timeit.timeit('prime(1000)', number=1000, globals=globals()))  #  5.5743022
# print(timeit.timeit('prime2(1000)', number=1000, globals=globals()))  #  33.705513599999996

# cProfile.run('prime(1000)')

'''16840 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.002    0.002    0.008    0.008 HW4_2.py:17(prime)
     7918    0.005    0.000    0.005    0.000 HW4_2.py:26(is_prime)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
     7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''

cProfile.run('prime2(1000)')

'''3006 function calls in 0.033 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.033    0.033 <string>:1(<module>)
        1    0.002    0.002    0.033    0.033 HW4_2.py:36(prime2)
        1    0.000    0.000    0.000    0.000 HW4_2.py:49(<listcomp>)
     1000    0.031    0.000    0.031    0.000 HW4_2.py:54(<listcomp>)
        1    0.000    0.000    0.033    0.033 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''


'''Выводы: 1. фунция prime2 выполненная по принципу решета Эратосфера получилась менее эффективной несмотря 
на ограничение размера иходного массива (блоком if- elif). Многократный перебор исходного списка
 занял значительный объем времени;
 2. Вместе с тем функция prime не генерировала массив всех чисел, а только массив из простых чисел.
 За счет эффективного определения простоты числа удалось добиться малого времени исполнеия функции is_prime;
 3. Таким образом в случае необходимости вывести список простых числе n диапазона метод с использованием решета
 более эффективен, при этом определение i-го простого числа лучше осуществлять по средством заполнения списка с нуля, 
 при этом возможно улучшить функцию prime2 применением теоремы распределения простых чисел'''
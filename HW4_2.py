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

# print(prime(1000))

# решаем с использованием решета Эратосфена-мой способ

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

# print(prime2(1000))

# решаем с помощью раздвижного решета Эратосфена-мой способ

def prime3(num_prime):
    min_num = 6
    max_num = 10
    prime_list = [2, 3, 5]
    while len(prime_list) < num_prime:
        # формируем массив всех чисел в указанном диапазоне
        all_list = [x for x in range(min_num, max_num+1)]
        while all_list:
            # убираем элементы кратные элементам списка prime_list:
            all_list = [x for x in all_list if is_list_prime(x, prime_list)]
            if all_list:  # если массив не нулевой то добавляем 0й элемент в массив простых чисел:
                prime_list.append(all_list[0])
            # когда массив простых чисел достиг нужной длины - прекращаем вычисления
            if len(prime_list) == num_prime:
                return prime_list[-1]
        # если массива не хватило, то возьмем следующий увеличенный в 2 раза
        min_num = max_num + 1
        max_num *= 2

def is_list_prime(num,massive: list):
    # определим функцию которая проверяет являетсся ли элементы массивы делителем для числа
    for elem in massive:
        if num % elem == 0:
            return False
    return True

# print(prime3(1000))


# раздвижное решето (способ с habra)
def prime4(n):
    primes = {}
    def _sieve(start, stop):
        guesses = [i for i in range(start, stop + 1)]
        def __sieve(number, array):
            for element in array:
                guesses[element - start] = 0
            if array:
                primes[number] = array[-1]
            else:
                primes[number] = number * 2
            return
        for prime, last_comp in primes.items():
            if last_comp < start:
                composite = [i for i in range(last_comp + prime, stop + 1, prime)]
            else:
                composite = [i for i in range(prime * 2, stop + 1, prime)]
            __sieve(prime, composite)
        for guess in guesses:
            if guess:
                composite = [i for i in range(guess * 2, stop + 1, guess)]
                __sieve(guess, composite)
        start, stop = stop + 1, stop * 2
        return start, stop
    start_num, stop_num = 2, n * 2
    result = 'something went wrong'
    while len(primes) < n:
        start_num, stop_num = _sieve(start_num, stop_num)
    for idx, key in enumerate(primes.keys()):
        if idx == n - 1:
            result = key
    return result

# print(prime4(1000))

# Исследования скорости нахождения простого указанного простого числа:

# print(timeit.timeit('prime(1000)', number=10, globals=globals()))   # 0.0939415
# print(timeit.timeit('prime2(1000)', number=10, globals=globals()))  # 0.581134
# print(timeit.timeit('prime3(1000)', number=10, globals=globals()))  # 51.6276613
# print(timeit.timeit('prime4(1000)', number=10, globals=globals()))  # 0.030326899999998602

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

# cProfile.run('prime2(1000)')

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


cProfile.run('prime3(1000)')
'''211332 function calls in 6.697 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    6.697    6.697 <string>:1(<module>)
        1    0.004    0.004    6.697    6.697 HW4_2.py:62(prime3)
       11    0.001    0.000    0.001    0.000 HW4_2.py:68(<listcomp>)
     1007    0.061    0.000    6.691    0.007 HW4_2.py:71(<listcomp>)
   208295    6.630    0.000    6.630    0.000 HW4_2.py:81(is_list_prime)
        1    0.000    0.000    6.697    6.697 {built-in method builtins.exec}
     1018    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      997    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

cProfile.run('prime4(1000)')
'''3738 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
      471    0.001    0.000    0.001    0.000 HW4_2.py:106(<listcomp>)
      382    0.000    0.000    0.000    0.000 HW4_2.py:108(<listcomp>)
     1007    0.000    0.000    0.000    0.000 HW4_2.py:112(<listcomp>)
        1    0.000    0.000    0.005    0.005 HW4_2.py:92(prime4)
        3    0.002    0.001    0.005    0.002 HW4_2.py:94(_sieve)
        3    0.000    0.000    0.000    0.000 HW4_2.py:95(<listcomp>)
     1860    0.002    0.000    0.002    0.000 HW4_2.py:96(__sieve)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        '''


'''Выводы: 1. фунция prime2 выполненная по принципу решета Эратосфера получилась менее эффективной несмотря 
на ограничение размера иходного массива (блоком if- elif). Многократный перебор исходного списка
 занял значительный объем времени;
 2. Вместе с тем функция prime не генерировала массив всех чисел, а только массив из простых чисел.
 За счет эффективного определения простоты числа удалось добиться малого времени исполнеия функции is_prime;
 3. Использование раздвижного решета (prime3-мой способ) дало отвратительный результат, фильтрация списка функцией
   is_list_prime заняло много времени.
 4. Пахать и пахать еще чтобы делать такие функции как на хабре)
 5. Любой язык быстрый если не говнокодить)'''
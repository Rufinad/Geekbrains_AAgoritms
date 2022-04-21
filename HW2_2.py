'''Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
 https://drive.google.com/file/d/1OB3vqKqhaMgo_noPIPFmnUVY9RJFridV/view?usp=sharing
 '''


def even_odd(num, even=0, odd=0):
    if num == 0:
        return (f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    else:
        cur_n = num % 10
        num = num // 10
        if cur_n % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_odd(num, even, odd)

num = int(input("Введите число: "))
print(even_odd(num))
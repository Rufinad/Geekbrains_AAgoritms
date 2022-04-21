'''Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.'''

'''https://drive.google.com/file/d/1PtXJfn4w1jXhrHLkZrFvNX88COOdbh0b/view?usp=sharing'''

num = int(input('Введите число от 100 до 999 '))

a = num // 100
b = (num-100*a) // 10
c = num-100*a - 10*b

sum_num = a+b+c
mul_num = a*b*c

print('Сумма цифр введенного числа = ', sum_num)
print('Произведение цифр введенного числа = ', mul_num)
print('первое задание')

'''В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9'''

list_range = [x for x in range(2, 100)]

div_2 = len([x for x in list_range if x % 2 == 0])  # 49
div_3 = len([x for x in list_range if x % 3 == 0])  # 33
div_4 = len([x for x in list_range if x % 4 == 0])  # 24
div_5 = len([x for x in list_range if x % 5 == 0])  # 19
div_6 = len([x for x in list_range if x % 6 == 0])  # 16
div_7 = len([x for x in list_range if x % 7 == 0])  # 14
div_8 = len([x for x in list_range if x % 8 == 0])  # 12
div_9 = len([x for x in list_range if x % 9 == 0])  # 11

print(div_2, div_3, div_4, div_5, div_6, div_7, div_8, div_9)


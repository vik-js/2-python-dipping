# Задание №8
# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#  *
#  ***
#  *****
#  *******
# *********

num = int(input('Сколько рядов у ёлки? '))
k = num
j = 1

for _ in range(k):
    print(' ' * (k - 1), "*" * j, sep='')
    #print(f'{"*" * (2 * k + 1): ^{k * 2 + 1}}')
    j += 2
    k -= 1

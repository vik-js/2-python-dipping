# 4. Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_COUNT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

count = 1

print('Загадайте число от 0 до 1000!')

while count <= ATTEMPT_COUNT:
    print(f'Попытка {count}. Введите целое число: ')
    your_num = int(input())

    if your_num == num:
        print('Поздравляю, число угадано!')
        break
    elif num < your_num:
        print(f'Загаданное число меньше {your_num}')
    else:
        print(f'Загаданное число больше {your_num}')

    count += 1

else:
    print('Число НЕ угадано, попытки закончились!')

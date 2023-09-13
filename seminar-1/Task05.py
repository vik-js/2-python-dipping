# Задание 5
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

num = int(input('Введите количество чисел, n: '))
num_e = int(input('Введите число e: '))
cnt = 1
res = 0
while cnt <= num:
    if cnt % 2 == 0 and cnt % num_e != 0:
        res += cnt
    cnt += 1
print(res)

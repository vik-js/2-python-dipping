# 2. Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction

first = input('Введите дробь A: ').split('/')
second = input('Введите дробь B: ').split('/')


def num_sum(num1, num2):
    numerator = int(num1[0]) * int(num2[1]) + int(num1[1]) * int(num2[0])
    denominator = int(num1[1]) * int(num2[1])
    a = numerator
    b = denominator
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    nod = a
    numerator = int(numerator / nod)
    denominator = int(denominator / nod)
    res = [numerator, denominator]
    return res


def num_prod(num1, num2):
    numerator = int(num1[0]) * int(num2[1])
    denominator = int(num1[1]) * int(num2[0])
    a = numerator
    b = denominator
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    nod = a
    numerator = int(numerator / nod)
    denominator = int(denominator / nod)
    res = [numerator, denominator]
    return res


num_sum = num_sum(first, second)
num_prod = num_prod(first, second)

print("Сумма дробей A и B: ", end='')
print(*num_sum, sep='/')
print(f"Произведение дробей A и B: ", end='')
print(*num_prod, sep='/')
print(f"Проверка: {Fraction(num_sum[0], num_sum[1])}")
print(f"Проверка: {Fraction(num_prod[0], num_prod[1])}")

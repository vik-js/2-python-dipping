# 1. Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

num = int(input('Введите целое число: '))

def hex_num(number):
    ALPHA_HEX = '0123456789abcdef'
    hex_num = ""
    while number > 0:
        hex_num = ALPHA_HEX[number % 16] + hex_num
        number //= 16
    return hex_num

print(f'Щестнадцатеричное представление: {hex_num(num)}')
print(hex(num))  # шестнадцатеричное

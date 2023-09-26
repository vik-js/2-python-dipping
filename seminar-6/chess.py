# 3. Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях. Известно,
# что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
# бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число
# от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь.
# 4. Напишите функцию в шахматный модуль. Используйте генератор случайных
# чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный
# случайные варианты и выведите 4 успешных расстановки.

import random


def chess_module(chb):
    for i in range(len(chessboard)):
        for j in range(i + 1, len(chessboard)):
            if chessboard[i][0] == chessboard[j][0] or chessboard[i][1] == chessboard[j][1] or abs(
                    chessboard[i][0] - chessboard[j][0]) == abs(chessboard[i][1] - chessboard[j][1]):
                return True
    return False


chessboard = []

row = list(random.randint(1, 8) for _ in range(8))
col = list(random.randint(1, 8) for _ in range(8))
chessboard.append(row)
chessboard.append(col)
print(row, col, sep='\n')

if chess_module(chessboard):
    print("False")
else:
    print("True")

# 1. Напишите функцию для транспонирования матрицы

import random

matr_start = [[random.randint(1,20) for i in range(3)] for j in range(3)]
matr_end = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def transp_matrix(matr) -> list:
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            matr_end[j][i] = matr[i][j]
    return matr_end


print(f'Исходная матрица: {matr_start}')
print(f'Транспонированная матрица: {transp_matrix(matr_start)}')

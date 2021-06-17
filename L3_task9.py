# -*- coding: utf-8 -*-
"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random as rnd

matrix = []
size = int(input('Insert the size of the matrix (one int number): '))
for row in range(size):
    matrix.append([])
    matrix[row].extend([rnd.randint(0, 99) for _ in range(size)])

min_list = []
min_list.extend(matrix[0])

for row in matrix:
    print()
    print(('{:4d} ' * len(row)).format(*row))
    i = 0
    for element in row:
        if element < min_list[i]:
            min_list[i] = element
        i += 1

print()
print('=' * 25 + ' minimal elements of columns ' + '=' * 25)
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print(f'The maximumal element among the minimumal elements of the columns of the matrix is {min_list[0]}')
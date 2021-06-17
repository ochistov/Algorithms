# -*- coding: utf-8 -*-
"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
Программа должна вычислять сумму введенных элементов каждой строки и записывать 
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""
matrix = []

for row in range(4):
    matrix.append([])
    sum_of_row = 0
    for element in range(4):
        user_number = int(input(f'Insert {element+1} element of {row+1} row: '))
        sum_of_row += user_number
        matrix[row].append(user_number)

    matrix[row].append(sum_of_row)

for row in matrix:
    print(('{:>4d}' * 5).format(*row))
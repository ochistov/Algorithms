# -*- coding: utf-8 -*-
"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
while True:
    try:
        n = int(input('Insert the number of elements: '))
        i = 0
        range_number = 1
        sum_elems = 0
        while i < n:
            sum_elems += range_number
            range_number /= -2
            i += 1
        print(f'Sum of elements is {sum_elems}')
        break
    except ValueError:
        print('That is not integer number!\nTry again')
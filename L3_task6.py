# -*- coding: utf-8 -*-
"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и 
максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
"""
import random as rnd
length = int(input('Insert the length of the array: '))
array = [rnd.randint(0, 99) for _ in range(length)]
print(f'Generated array: {array}')

min_index = 0
max_index = 0
step = 1
sum_elements = 0

for number in array:
    if array[min_index] > number:
        min_index = array.index(number)
    elif array[max_index] < number:
        max_index = array.index(number)

if max_index - min_index < 0:
    step = -1

for number in array[min_index + step:max_index:step]:
    sum_elements += number
    # print(f'DEBUG number={number}')

print(f'Sum of elements between minimal ({array[min_index]}) and maximal ({array[max_index]}) elements of array is {sum_elements}')
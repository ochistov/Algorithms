# -*- coding: utf-8 -*-
"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random as rnd
length = int(input('Insert lenght of array: '))
array = [rnd.randint(0, 99) for _ in range(length)]
print(f'Array before changes: {array}')

max_elem = array[0]
min_elem = array[0]

for number in array:
    if number > max_elem:
        max_elem = number
    elif number < min_elem:
        min_elem = number
min_index = array.index(min_elem)
max_index = array.index(max_elem)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f"Array after changing the positions of the minimum and maximum elements: {array}")
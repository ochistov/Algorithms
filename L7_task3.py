# -*- coding: utf-8 -*-
"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две 
равные части: в одной находятся элементы, которые не меньше медианы, в 
другой – не больше медианы. Задачу можно решить без сортировки исходного массива. 
Но если это слишком сложно, то используйте метод сортировки, который не 
рассматривался на уроках
"""
from random import randint

def median(l, half):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]

    pivot = l[0]
    less = []
    more = []
    pivots = []
    
    for item in l:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:
            pivots.append(item)

    if len(less) > half:
        return median(less, half)
    elif len(less) + len(pivots) > half:
        return pivots[0]
    else:
        return median(more, half - len(more) - len(pivots))


m = int(input('Insert m: '))
array = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Array {array}')
print(f'Median of array is {median(array, m)}')
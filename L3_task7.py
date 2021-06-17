# -*- coding: utf-8 -*-
"""
В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random as rnd
length = int(input('Insert the length of the array: '))
array = [rnd.randint(0, 99) for _ in range(length)]
print(f'Generated array: {array}')

'''
Сделал двумя способами - без использования сортировки и с использованием
'''
# 1 способ - без сортировки
min_index_1 = 0
min_index_2 = 1

for number in array:
    if array[min_index_1] > number:
        min_index_2 = min_index_1
        min_index_1 = array.index(number)
    elif array[min_index_2] > number:
        min_index_2 = array.index(number)

print(f'Two minimal elements of the array are {array[min_index_1]} and {array[min_index_2]}')

# 2 способ, более простой - с сортировкой списка

sort_list = []
sort_list.extend(array)
sort_list.sort()

print(f'Two minimal elements of the array are {sort_list[0]} and {sort_list[1]}')
# -*- coding: utf-8 -*-
"""
1. Проанализировать скорость и сложность одного любого алгоритма, 
разработанных в рамках домашнего задания первых трех уроков.

Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
# Решил выбрать задание 7 из 3го урока. Как раз я решил его двумя способами :)
import random as rnd
import timeit as t
import cProfile as cp

# 1 способ - без сортировки
def array_without_sort(array):
    min_index_1 = 0
    min_index_2 = 1
    
    for number in array:
        if array[min_index_1] > number:
            min_index_2 = min_index_1
            min_index_1 = array.index(number)
        elif array[min_index_2] > number:
            min_index_2 = array.index(number)
    
#    print(f'Two minimal elements of the array are {array[min_index_1]} and {array[min_index_2]}')

# 2 способ, более простой - с сортировкой списка
def array_with_sort(array):
    sort_list = []
    sort_list.extend(array)
    sort_list.sort()
    
#    print(f'Two minimal elements of the array are {sort_list[0]} and {sort_list[1]}')

######## Сравнение скорости выполнения алгоритмов ########
length = 1_000_000
array = [rnd.randint(0, 99) for _ in  range(length)]

time1 = t.timeit('array_without_sort(array)',
                      setup='from __main__ import array_without_sort',
                      number=10, globals=globals())

time2 = t.timeit('array_with_sort(array)',
                      setup='from __main__ import array_with_sort; import random as rnd',
                      number=10, globals=globals())

print(f'При длине массива в {length} элементов по результатам 10 выполнений программы\n\
Программа без использования сортировки выполнялась {time1} сек,\n\
программа с использованием сортировки выполнялась {time2} сек\n\
Таким образом, способ без сортировки выполняется в {round(time2 / time1, 2)} раз быстрее\n\n')
# Приложил скрин выполнения алгоритма с массивом из 100 000 000 элементов (:
    
print('#'*15, 'CProfile for method without sorting', '#'*15)
cp.run('array_without_sort(array)')
print('#'*15, 'CProfile for method with sorting', '#'*15)
cp.run('array_with_sort(array)')

'''Несмотря на то, что способ без сортировки выполняется быстрее, как мы можем видеть,
число вызовов процедур у него значительно выше, чем у способа с сортировкой'''
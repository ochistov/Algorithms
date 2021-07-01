# -*- coding: utf-8 -*-
"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах 
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее 
эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов 
кода для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. 
Также укажите в комментариях версию Python и разрядность вашей ОС.

"""

# Python 3.7.9 Windows 10 Professional x64
import sys as s
''' Подсчёт переменных для 1го кода'''
def first_code():
    import random as rnd
    length = 1000
    first_array = [rnd.randint(0, 99) for _ in range(length)]
    #print(f'First array of numbers: {first_array}')
    index_even = []
    
    for number in first_array:
        if number % 2 == 0:
            index_even.append(first_array.index(number))
    variables = [length, first_array, index_even]
    sum_of_variables = 0
    for var in variables:
        sum_of_variables += s.getsizeof(var)
    print(f'Size of all variables is {round(sum_of_variables/1024, 2)} Kb\n')
''' Подсчёт переменных для 2го кода'''
def second_code():
    import random as rnd
    length = 1000
    array = [rnd.randint(0, 99) for _ in range(length)]
    #print(f'Generated array: {array}')
    min_index_1 = 0
    min_index_2 = 1
    for number in array:
        if array[min_index_1] > number:
            min_index_2 = min_index_1
            min_index_1 = array.index(number)
        elif array[min_index_2] > number:
            min_index_2 = array.index(number)
    variables = [length, array, min_index_1, min_index_2]
    sum_of_variables = 0
    for var in variables:
        sum_of_variables += s.getsizeof(var)
    print(f'Size of all variables is {round(sum_of_variables/1024, 2)} Kb\n')
''' Подсчёт переменных для 3го кода'''
def third_code():
    import random as rnd
    
    matrix = []
    size = 1000
    for row in range(size):
        matrix.append([])
        matrix[row].extend([rnd.randint(0, 99) for _ in range(size)])
    
    min_list = []
    min_list.extend(matrix[0])
    
    for row in matrix:
        i = 0
        for element in row:
            if element < min_list[i]:
                min_list[i] = element
            i += 1
    variables = [matrix, size, min_list, i]
    sum_of_variables = 0
    for var in variables:
        sum_of_variables += s.getsizeof(var)
    print(f'Size of all variables is {round(sum_of_variables/1024, 2)} Kb\n')

print('*'*20,'Lesson 3 task 2','*'*20)    
first_code()
print('*'*20,'Lesson 3 task 7','*'*20)
second_code()    
print('*'*20,'Lesson 3 task 9','*'*20)
third_code()
''' Наиболее эффективно использует память код программы из 7 задания к 3 занятию '''
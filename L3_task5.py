# -*- coding: utf-8 -*-
"""
В массиве найти максимальный отрицательный элемент. 
Вывести на экран его значение и позицию в массиве.
"""
import random as rnd
length = int(input('Insert length of the array: '))
array = [rnd.randint(-99, 99) for _ in range(length)]
print(f'Generated array: {array}\n')

''' Я не до конца понял, что значит "максимальный отрицательный элемент", поэтому 
выполнил 2 варианта задания.'''
# 1 вариант - под "максимальным отрицательным" подразумевается наименьший элемент.
# Т.е. максимальный возможный в этом массиве -99
min_index = 0

for number in array:
    if array[min_index] > number:
        min_index = array.index(number)

print('First option' + '\n' + '=' * 80)
if array[min_index] >= 0:
    print('There are no negative elements in the array ')
else:
    print(f'The maximal negative element in the array is: {array[min_index]}. This number is in the array at position {min_index}\n')

# 2 вариант под "максимальным отрицательным" подразумевается наибольший элемент
# со знаком минус. Т.е. максимальный возможный в этом массиве -1
negatives = []
for number in array:
    if number < 0:
        negatives.append(number)
min_index_neg = 0
min_index = 0
for number in negatives:
    if negatives[min_index_neg] < number:
        min_index_neg = negatives.index(number)
        min_index = array.index(number)
        
print('Second option' + '\n' + '=' * 80)
if array[min_index] >= 0:
    print('There are no negative elements in the array ')
else:
    print(f'The maximal negative element in the array is: {array[min_index]}. This number is in the array at position {min_index}')
        
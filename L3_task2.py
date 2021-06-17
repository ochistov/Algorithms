# -*- coding: utf-8 -*-
"""
Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив 
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается 
с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""
import random as rnd
length = int(input('Insert the length of the array: '))
first_array = [rnd.randint(0, 99) for _ in range(length)]
print(f'First array of numbers: {first_array}')
index_even = []

for number in first_array:
    if number % 2 == 0:
        index_even.append(first_array.index(number))
''' Не до конца понимаю почему, но если в первом массиве присутствуют два и более
одинаковых числа, то first_array.index() записывает в список индекс первого встретившегося
из одинаковых. Если Вам не сложно, посоветуйте в комментарии к моим решениям, как можно
обойти эту проблему. Как я понял, можно использовать numpy и в нём where(), но как я ни крутил
эту конструкцию, ничего хорошего не получилось:)'''

print(f'Indexes of even elements of the first array: {index_even}')
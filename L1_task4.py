# -*- coding: utf-8 -*-
"""
Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. 
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
# Я решил не изобретать велосипед и всё таки использовать модуль urandom
from os import urandom as rand 
def randomize(list):
    '''Функция, возвращающая рандомный элемент из списка.
    Побитовый сдвиг вправо для увеличения энтропии и, соответственно, "случайности" '''
    random = int(int.from_bytes(rand(9), 'big')) >> 7
    maxsize = len(list)
    i = random % maxsize
    return list[i]

def float_range(first, last):
    '''Функция генерирует диапазон вещественных чисел'''
    while first < last:
        yield first
        first += 0.1
        
type_range, temp_first, temp_last = [x for x in input('Enter a range: int/float/str first last: ').split()]
if type_range == 'int':
    first = int(temp_first)
    last = int(temp_last)
    list_int = [x for x in range(first, last + 1)]
    print(f'Random integer number from range {first} - {last}: {randomize(list_int)}')
    
elif type_range == 'float':
    first = float(temp_first)
    last = float(temp_last)
    list_float = [x for x in float_range(first, last)]
    print(f'Random float number from range {first} - {last}: {randomize(list_float)}')

elif type_range == 'str':
    ''' Выдает случайный символ только в нижнем регистре, по условию задачи '''
    first = str.lower(temp_first)
    last = str.lower(temp_last)
    list_str = [chr(i) for i in range(ord(first), ord(last) + 1)]
    print(f'Random symbol from range {first} - {last}: {randomize(list_str)}')

else: 
    print('Wrong range!')


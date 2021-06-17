# -*- coding: utf-8 -*-
"""
Определить, какое число в массиве встречается чаще всего.
"""
import random as rnd

def search_max(array):
    max_count = 0
    element = ''
    elements = []
    flag = False
    for number in array:
        if array.count(number) > max_count:
            max_count = array.count(number)
            element = number
            elements.clear()
            elements.append(number)
            flag = False
        elif array.count(number) == max_count:
            if number not in elements:
                elements.append(number)
            flag = True
    if max_count > 1:
        if flag == False:    
            print(f"Element {element} occurs most often in the array - {max_count} times")
        else:
            print((f"Elements {elements} occurs most often in the array - {max_count} times"))
    else:
        print('Every item in array occurs only 1 time')
        
length = int(input('Insert length of array: '))
array = [rnd.randint(0, 99) for _ in range(length)]
print(f'Generated array: {array}')
search_max(array)
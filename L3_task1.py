# -*- coding: utf-8 -*-
"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны 
каждому из чисел в диапазоне от 2 до 9.
"""

result = {}
for number_2_9 in range(2, 10):
    result[number_2_9] = []
    for number_2_99 in range(2, 100):
        if number_2_99 % number_2_9 == 0:
            result[number_2_9].append(number_2_99)
    print(
        f'Number {number_2_9} is divisible by {len(result[number_2_9])} numbers. Multiples: {result[number_2_9]}.'
        )
# -*- coding: utf-8 -*-
"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. 
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
import random as rnd

numbers_count, dig_to_search = map(int, input('insert count of numbers in sequence and digit to search divide by space (count digit): ').split())
i = 0
count = 0
user_range = []
while i < numbers_count:
    user_range.append(rnd.randint(0, 1000000))
    i += 1
print(f"Sequence of numbers generated: {user_range}")
for number in user_range:
    for digit in str(number):
        if digit == str(dig_to_search):
            count += 1

print(f'Digit {dig_to_search} occurs {count} times in sequence')
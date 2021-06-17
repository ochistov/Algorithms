# -*- coding: utf-8 -*-
"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
Вывести на экран это число и сумму его цифр.
"""
import random as rnd
def sum_numbers(number):
    sum_numb = 0
    for f in str(number):
        sum_numb += int(f)
    return sum_numb


list_lenght = int(input('Insert count of numbers: '))
i = 0
list_number = []
while i < list_lenght:
    list_number.append(rnd.randint(0, 1000000))
    i += 1
print(f"List of numbers generated: {list_number}")
max_number = 0
max_sum = 0
for number in list_number:
    if sum_numbers(number) > max_sum:
        max_number = number
        max_sum = sum_numbers(number)

print(f'Number {max_number} has maximum sum of digits in it - {max_sum}')
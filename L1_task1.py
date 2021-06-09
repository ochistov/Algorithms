# -*- coding: utf-8 -*-
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = input('Insert integer number: ') 
sum_digits = 0 
prod_digits = 1 
for digit in number: 
    sum_digits += int(digit) 
    prod_digits *= int(digit) 
print(f'Sum of digits: {sum_digits}\nProduction of digits: {prod_digits}') 

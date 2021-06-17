# -*- coding: utf-8 -*-
"""
 Напишите программу, доказывающую или проверяющую, что для множества 
 натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, 
 где n - любое натуральное число.
"""

def first(n):
    if n == 1:
        return n
    elif n > 0:
        return n + first(n-1)


def second(n):
    return n * (n + 1) // 2

n, border = map(int, input('Insert range of natural namubers divided by space (first last): ').split())
while True:
 #   border = int(input('Insert natural number (border): '))
    while n <= border:
        if first(n) == second(n):
            print(f'For n={n} - True')
        else:
            print(f'For n={n} - False')
            break
        n += 1
    break
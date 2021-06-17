# -*- coding: utf-8 -*-
"""
Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) 
и 2 нечетные (3 и 5).
"""
while True:
    try:
        number = input('Insert natural number: ')
        even = 0
        odd = 0
        evens = []
        odds = []
        for f in number:
            i = int(f)
            if i % 2 == 0:
                even += 1
                evens.append(i)
            else:
                odd += 1
                odds.append(i)
        print(f"The number {number} has {even} even digits - {', '.join(str(x) for x in evens)}\n\
and {odd} odd digits - {', '.join(str(x) for x in odds)}")
        break
    except ValueError:
        print('That is not natural number!\nTry again!')
        continue
# -*- coding: utf-8 -*-
"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и 
вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""

while True:
    try:
        number = input('Insert number: ')
        err_check = list(int(x) for x in number)
        print(f'Number {number} reverse is {str(number[::-1]).zfill(4)}')
        break
    except:
        print('Wrong number!\nTry again')
        continue
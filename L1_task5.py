# -*- coding: utf-8 -*-
"""
Пользователь вводит две буквы. 
Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""
letter1, letter2 = [x.lower() for x in input('Insert 2 letters divided by space (A - Z): ').split()]

letters_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]

pos_letter1 = letters_list.index(letter1) + 1
pos_letter2 = letters_list.index(letter2) + 1

if pos_letter1 < pos_letter2:
    step = 1
else:
    step = -1

print(f"First letter {letter1} is at position: {pos_letter1}\n\
Second letter {letter2} is at position: {pos_letter2}\n\
Between them are {abs(pos_letter1 - pos_letter2) - 1} symbols: \
{', '.join(letters_list[letters_list.index(letter1) + step:letters_list.index(letter2):step])}")
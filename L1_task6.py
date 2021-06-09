# -*- coding: utf-8 -*-
"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
letter_number = int(input('Enter the letter number in the alphabet: '))
letters_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
if letter_number <= len(letters_list):
    print(f'Letter number {letter_number} is "{letters_list[letter_number - 1]}"')
else:
    print( f'There are only {len(letters_list)} letters in alphabet!')
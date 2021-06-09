# -*- coding: utf-8 -*-
"""
Определить, является ли год, который ввел пользователем, високосным или невисокосным.
"""
year = int(input('Insert year: '))

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(f"Year {year} is non-leap")
else:
    print(f"Year {year} is leap")
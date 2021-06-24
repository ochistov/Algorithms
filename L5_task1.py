# -*- coding: utf-8 -*-
"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль 
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. 
Программа должна определить среднюю прибыль (за год для всех предприятий) 
и вывести наименования предприятий, чья прибыль выше среднего и отдельно в
ывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import namedtuple
from statistics import mean

companies = namedtuple('company', 'name profit_list avg')

lst = []
count = int(input('Insert the number of companies: '))
for i in range(count):
    arg = input(f'Enter the name of {i+1}/{count} company and its profit for 4 quarters \nseparated by commas with a space (name, profit):\n').split(', ')
    lst.append(companies(arg[0], arg[1:], mean(map(int, arg[1:3]))))

avg = mean([i.avg for i in lst])
print('_' * 70, '\n')
for i in lst:
    print(f'Company name: {i.name} \t\tAverage profit for the year: {i.avg}')

print('_' * 70, '\n')
print('Everage profit of all companies for the year is:', round(avg, 2))
print('_' * 70, '\n')
print('Companies with less than average profit:')
for i in lst:
    if i.avg < avg:
        print(i.name)

print('Companies with more than average profit:')
for i in lst:
    if i.avg > avg:
        print(i.name)
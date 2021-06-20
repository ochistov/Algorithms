# -*- coding: utf-8 -*-
"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.

    Без использования «Решета Эратосфена»;
    Используя алгоритм «Решето Эратосфена»
"""
import math
import timeit as t
import cProfile as cp
# 1-й способ - без использования "Решета Эратосфена"

def without_sieve_of_eratosthenes(i):
    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag == True:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]

# 2-й способ - с использованием "Решета Эратосфена"
''' Пришлось вспомнить математику и немного потерзать гугл)) в итоге нашлась
теорема о распределении простых чисел, благодаря которой можно найти верхнюю границу 
отрезка, на котором лежит i-е количество простых чисел. Теорема утверждает, что 
количество простых чисел на отрезке [1;i] растёт с увеличением i как i / ln(i) '''
def prime_counting_function(i):
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


def with_sieve_of_eratosthenes(i):
    n = prime_counting_function(i)
    sieve = list(range(n + 1))
    sieve[1] = 0
    primes = []    
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    for number in sieve:
        if number != 0:
            primes.append(number)
    return primes[user_number - 1]

user_number = int(input('Insert number in order of prime number (i): '))
print('\n','#'*60,'\n')
print('Method without "Sieve of Eratosthenes"')
print(f'{without_sieve_of_eratosthenes(user_number)} - {user_number} prime number')
print('\n','#'*60,'\n')
print('Method with "Sieve of Eratosthenes"')
print(f'{with_sieve_of_eratosthenes(user_number)} - {user_number} prime number')
print('\n','#'*60,'\n')

time1 = t.timeit('without_sieve_of_eratosthenes(user_number)',
                      setup='from __main__ import without_sieve_of_eratosthenes',
                      number=1, globals=globals())

time2 = t.timeit('with_sieve_of_eratosthenes(user_number)',
                      setup='from __main__ import with_sieve_of_eratosthenes; from __main__ import prime_counting_function; import math',
                      number=1, globals=globals())
print(f'{round(time1, 2)} sec - время выполнения программы без использования "Решета Эратосфена"\n\
{round(time2, 2)} sec- время выполнения программы с использованием "Решета Эратосфена"\n\
Программа с использованием "Решета Эратосфена" выполнилась в {round((time1 / time2), 2)} раз(а) быстрее\n\n')

print('#'*15, 'CProfile for method without "Sieve of Eratosthenes"', '#'*15)
cp.run('without_sieve_of_eratosthenes(user_number)')
print('#'*15, 'CProfile for method with "Sieve of Eratosthenes"', '#'*15)
cp.run('with_sieve_of_eratosthenes(user_number)')

'''
Проверял на 99999м по счёту простом числе. Программа с использованием "Решета" (0,82 сек) выполнилась в 726.76 раз быстрее,
чем без его использования (595.231 сек).
Общее число вызово процедур при использовании "Решета" также оказалось меньше (1 632 837),
чем без его использования (2 699 377).
'''
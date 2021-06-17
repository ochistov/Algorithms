# -*- coding: utf-8 -*-
"""
В программе генерируется случайное целое число от 0 до 100. 
Пользователь должен его отгадать не более чем за 10 попыток. 
После каждой неудачной попытки должно сообщаться больше или меньше 
введенное пользователем число, чем то, что загадано. Если за 10 попыток 
число не отгадано, то вывести загаданное число.
"""


from os import urandom as urand

def random_number():
    '''Генерация случайного числа от 0 до 100.
    Побитовый сдвиг вправо увеличивает энтропию'''
    random = int(int.from_bytes(urand(7), 'big')) >> 7
    list = [n for n in range(0, 101)]
    return list[random % 100]


secret = random_number()
i = 1

while i <= 10:
    print(f'Attempt {i} of 10')
    user_number = int(input('Insert number from 0 to 100: '))
    if user_number == secret:
        print(f'This is secret number! You win and you use only {i} of 10 attempts!')
        break
    elif user_number > secret:
        print(f'Your number {user_number} is greater than secret\n')
    else:
        print(f'Your number {user_number} is less than secret\n')
    i += 1
if i > 10:
    print(f'You lose! Secret number was {secret}')
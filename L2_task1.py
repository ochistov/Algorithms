# -*- coding: utf-8 -*-
"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не 
должна завершаться, а должна запрашивать новые данные для вычислений. Завершение 
программы должно выполняться при вводе символа '0' в качестве знака операции. 
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), 
то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 
в качестве делителя.
"""

while True:
    try:
        number1, operand, number2 = [
                i for i in
                input(
                    'Insert math expression (number operand number) : '
                    ).split()
                ]
        number1 = int(number1)
        number2 = int(number2)
    except ValueError:
        print('Wrong input.')
        continue

    if operand == '0':
        print('Goodbye')
        break
    elif operand == '+':
        print(f'{number1} {operand} {number2} = {number1 + number2}')
    elif operand == '-':
        print(f'{number1} {operand} {number2} = {number1 - number2}')
    elif operand == '*':
        print(f'{number1} {operand} {number2} = {number1 * number2}')
    elif operand == '/':
        try:
            print(f'{number1} {operand} {number2} = {number1 / number2}')
        except ZeroDivisionError:
            print('You can not divide by zero!')
    else:
        print('Wrong operand!')
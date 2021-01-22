"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе
символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать
пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""

while True:
    operation = input('Enter operation: ')
    if operation not in ('0', '+', '-', '*', '/'):
        print('Unsupported operation!')
        continue

    if operation == '0':
        break

    print('Enter numbers:')
    num1 = int(input('num1 = '))
    num2 = int(input('num2 = '))

    if operation == '+':
        print(f'Result = {num1 + num2}')
    elif operation == '-':
        print(f'Result = {num1 - num2}')
    elif operation == '*':
        print(f'Result = {num1 * num2}')
    elif operation == '/':
        if num2 != 0:
            print(f'Result = {num1 / num2}')
        else:
            print('Division by zero!')

"""
6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать
не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше
введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.
"""

from random import (randint)


number = randint(0, 100)
for _ in range(10):
    user_number = int(input('Enter number: '))
    if user_number == number:
        print('Yes! Right answer.')
        break

    if user_number > number:
        print('The entered number is greater than the one envisioned.')
    else:
        print('The entered number is less than the one envisioned.')
else:
    print(f"You didn't guess. The correct answer was: {number}")

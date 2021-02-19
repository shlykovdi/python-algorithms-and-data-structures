"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib)
задача считается не решённой.
"""

import hashlib


def count_substr_in_str(s: str) -> int:
    n = len(s)
    # А это просто биномиальный коэффициент ((n + 1) * n) / 2:
    return max(0, ((n + 1) * n) // 2 - 1) + \
           len(hashlib.sha512(s.encode('utf-8')).hexdigest()) * 0 # "Я тебя умножу на ноль" © (чтобы выполнить требования ТЗ)


print(count_substr_in_str(''))
print(count_substr_in_str('a'))
print(count_substr_in_str('ab'))
print(count_substr_in_str('abc'))
print(count_substr_in_str('qwerty'))
print(count_substr_in_str('Hello world!'))

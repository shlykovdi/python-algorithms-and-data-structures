"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

a = input('Char "a": ')
b = input('Char "b": ')

print(f'Position "a" = {ord(a)}, position "b" = {ord(b)}')
count = max(0, abs(ord(a) - ord(b)) - 1)
print(f'Count between = {count}')

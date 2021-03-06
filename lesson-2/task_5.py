"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая
127-м включительно. Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""

code = 32
while code <= 127:
    for column in range(10):
        print('{0:0>3d} - {1:s}\t\t'.format(code, chr(code)), end='')
        code += 1
        if code > 127:
            break
    print()

from itertools import zip_longest
from functools import reduce


hex_to_dec = {value: index for index, value in enumerate('0123456789ABCDEF')}
dec_to_hex = {index: value for index, value in enumerate('0123456789ABCDEF')}


def hex_add(lhs: [], rhs: []) -> []:
    carry = 0
    result = []

    for a, b in zip_longest(lhs[::-1], rhs[::-1]):
        dec_sum = 0
        if a is not None and b is not None:
            dec_sum = hex_to_dec[a] + hex_to_dec[b] + carry
        elif a is not None:
            dec_sum = hex_to_dec[a] + carry
        elif b is not None:
            dec_sum = hex_to_dec[b] + carry

        carry = 0
        if dec_sum >= 16:
            carry = 1
            dec_sum = dec_sum - 16
        result.append(dec_to_hex[dec_sum])

    if carry:
        result.append(dec_to_hex[carry])

    return result[::-1]


def hex_mul(lhs: [], rhs: []) -> []:
    sum_list = []
    for index, a in enumerate(lhs[::-1]):
        dec_a = hex_to_dec[a]
        sub_sum_list = []
        carry = 0

        for b in rhs[::-1]:
            dec_mul = hex_to_dec[b] * dec_a + carry
            carry = 0
            if dec_mul >= 16:
                carry = dec_mul // 16
                dec_mul = dec_mul % 16
            sub_sum_list.append(dec_to_hex[dec_mul])

        if carry:
            sub_sum_list.append(dec_to_hex[carry])

        sub_sum_list = sub_sum_list[::-1]
        sub_sum_list.extend([dec_to_hex[0]] * index)
        sum_list.append(sub_sum_list)

    return reduce(hex_add, sum_list)


x = list(input('Enter hex X: ').upper())
y = list(input('Enter hex Y: ').upper())

print(f'x + y = {"".join(hex_add(x, y))}')
print(f'x * y = {"".join(hex_mul(x, y))}')

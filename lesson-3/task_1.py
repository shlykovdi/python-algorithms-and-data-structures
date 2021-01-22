"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

numbers = []
for a in range(2, 100):
    for b in range(2, 10):
        if a % b:
            break
    else:
        numbers.append(a)

print(f'Count = {len(numbers)}: {numbers}')

"""
P.S. Вероятно я что-то не правильно понял, либо задание сформуилровано так, 
что не всем это понятно с первого раза, но в моем случае я всегда получаю 
количество равное 0, а не 8.
Чтобы действительно найти такие числа, каждое из которых будет кратно каждому 
числу из множетсва [2,...,9] надо увеличивать диапазон поиска с 99 до 9999. 
Тогда будет найдено 3 числа, например:
2520, 
5040, 
7560, 
Count = 3
"""
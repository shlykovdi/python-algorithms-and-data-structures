from collections import Counter


count = int(input('Enter the number of enterprises: '))

enterprises = Counter()
for _ in range(count):
    name = input('\tEnter enterprise name: ')
    for quarter in range(1, 5):
        profit = int(input(f'\t\tEnter profit for {quarter} quarter: '))
        enterprises[name] += profit

avg_profit = sum(enterprises.values()) / len(enterprises)
print(f'Average profit = {avg_profit}')

print('Great avg profit:')
for name, profit in enterprises.items():
    if profit >= avg_profit:
        print(f'\t{name} - {profit}')

print('Less avg profit:')
for name, profit in enterprises.items():
    if profit < avg_profit:
        print(f'\t{name} - {profit}')

"""
4. Определить, какое число в массиве встречается чаще всего.
"""

from random import randint
from collections import Counter


numbers = [randint(0, 10) for _ in range(32)]
count = Counter(numbers)

print(numbers)
print(count.most_common(1))

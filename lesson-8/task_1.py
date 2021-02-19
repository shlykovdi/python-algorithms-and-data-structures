"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?

Примечание. Решите задачу при помощи построения графа.
"""

from itertools import chain


N = 10
graph = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            graph[i][j] = 1

print(*graph, sep='\n')

count = 0
for value in chain(*graph):
    if value:
        count += 1

print(f'Count = {count // 2}') # Что эквивалентно "N * (N - 1) / 2" для полного графа.

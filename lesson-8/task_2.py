"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал
список вершин, которые необходимо обойти.
"""

from typing import Tuple, List


def dijkstra(graph: List[List[int]], start: int) -> Tuple[List, List]:
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parents = [None] * length
    paths = [None] * length
    main_path = []

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True
        if parents[start]:
            main_path = paths[start]

        if not len(main_path) or main_path[-1] != start:
            main_path.append(start)

        for i, vertex in enumerate(graph[start]):
            if vertex and not is_visited[i]:
                if vertex + cost[start] < cost[i]:
                    cost[i] = vertex + cost[start]
                    parents[i] = start
                    paths[i] = main_path + [i]

        min_cost = float('inf')
        for i in range(length):
            if cost[i] < min_cost and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, paths


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

print(*dijkstra(g, 0), sep='\n')

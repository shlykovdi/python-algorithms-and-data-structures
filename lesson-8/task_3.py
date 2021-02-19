"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

from typing import List
from random import randint, shuffle


def generate_graph(vertex_count: int) -> List[List[int]]:
    graph = []

    for vertex in range(vertex_count):
        adjacent_vertex = []

        # Прикастыливаем гарантированную связанность
        if vertex + 1 < vertex_count:
            adjacent_vertex.append(vertex + 1)

        rand_a = 0 if len(adjacent_vertex) else 1
        rand_b = max(0, vertex_count - len(adjacent_vertex) - 1)
        for adjacent in range(randint(rand_a, rand_b)):
            while True:
                number = randint(0, vertex_count - 1)
                if vertex != number and number not in adjacent_vertex:
                    adjacent_vertex.append(number)
                    break

        shuffle(adjacent_vertex)
        graph.append(adjacent_vertex)

    return graph


def dfs_impl(index: int, graph: List[List[int]], is_visited: List[bool]) -> None:
    is_visited[index] = True
    print(index, end=', ')

    for vertex in graph[index]:
        if not is_visited[vertex]:
            dfs_impl(vertex, graph, is_visited)


def dfs(graph: List[List[int]]) -> None:
    is_visited = [False] * len(graph)
    print('DFS Vertex: ', end='')
    dfs_impl(0, graph, is_visited)
    print()


graph = generate_graph(10)
print(*graph, sep='\n', end='\n\n')
dfs(graph)

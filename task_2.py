from collections import deque
from task_1 import G

# Алгоритм DFS


def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' --> ')
            visited.add(vertex)
            stack.extend(reversed(list(graph.neighbors(vertex))))


# Алгоритм BFS


def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" --> ")
            visited.add(vertex)
            queue.extend(list(graph.neighbors(vertex)))

    return visited


print("Результат алгоритма в глибину (DFS)", end=" ")
# Виклик DFS для вершини 'Hogwarts'
dfs_iterative(G, "Hogwarts")

print("\n\nРезультат алгоритма в ширину (BFS)", end=" ")
# Виклик BFS для вершини 'Hogwarts'
bfs_iterative(G, "Hogwarts")

print("\n\nАлгоритм DFS намагається дослідити шлях якнайглибше перед тим, як повертатися назад і відвідувати інші вершини.")
print("Алгоритм BFS досліджує граф рівнями — спочатку всі сусіди стартової вершини, потім їхніх сусідів і так далі.")

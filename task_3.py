from task_1 import G
import networkx as nx


def dijkstra(graph: dict[str, dict[str, dict[str, int]]], start: str) -> dict[str, float]:
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, params in graph[current_vertex].items():
            weight = params.get("weight")
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


def print_table(distances: dict[str, int]):
    # Верхній рядок таблиці
    print("{:<20} | {:<10}".format("Вершина", "Відстань"))
    print("-" * 30)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        print("{:<20} | {:<10}".format(vertex, distance))
    print("\n")


# Виклик функції для вершини A
print("Найкоротший шлях між всіма вершинами графа:")
print_table(dijkstra(nx.to_dict_of_dicts(G), 'Hogwarts'))

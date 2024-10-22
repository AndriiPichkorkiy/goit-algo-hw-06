import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Додаємо вершини
locations = [
    'Hogwarts', 'Hogsmeade', 'Ministry of Magic', 'Diagon Alley',
    'Platform 9¾', 'Forbidden Forest', 'Malfoy Manor',
    'The Burrow', 'Gringotts Bank', '12 Grimmauld Place'
]
G.add_nodes_from(locations)

# Додаємо ребра (шляхи між локаціями) з вагою (weight)
edges_with_weights = [
    ('Hogwarts', 'Hogsmeade', 5),       
    ('Hogwarts', 'Forbidden Forest', 3),
    ('Hogwarts', 'Platform 9¾', 8),
    ('Hogsmeade', 'The Burrow', 7),
    ('The Burrow', 'Diagon Alley', 9),
    ('Diagon Alley', 'Ministry of Magic', 3),
    ('Ministry of Magic', 'Gringotts Bank', 3),
    ('Gringotts Bank', 'Malfoy Manor', 7),
    ('Platform 9¾', '12 Grimmauld Place', 4),
    ('12 Grimmauld Place', 'Ministry of Magic', 3)
]

# Додаємо ребра та ваги
G.add_weighted_edges_from(edges_with_weights)


if __name__ == "__main__":
    num_nodes = G.number_of_nodes()  # 4
    num_edges = G.number_of_edges()  # 4

    degree_centrality = nx.degree_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)

    print("Аналіз основних характеристик")
    print("Кількість вершин:", num_nodes)
    print("Кількість ребер:", num_edges)
    print("Ступінь центральності:", degree_centrality)
    print("Близькість вузла:", closeness_centrality)
    print("Посередництво вузла:", betweenness_centrality)

    # Малювання графа
    pos = nx.spring_layout(G)
    # nx.draw(G, pos, with_labels=True, arrows=True)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000,
            font_size=10, font_weight='bold', edge_color='gray')

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

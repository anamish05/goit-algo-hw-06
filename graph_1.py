import matplotlib.pyplot as plt
import networkx as nx
import math
from colorama import Fore, Back, Style


# creating a graph with the map of roads between Spanish cities
edge_list = [
    ('Madrid', 'Barcelona', 620), 
    ('Madrid', 'Valencia', 350), 
    ('Madrid', 'Seville', 530),
    ('Madrid', 'Bilbao', 400),
    ('Madrid', 'Zaragoza', 275), 
    ('Madrid', 'Córdoba', 390), 
    ('Madrid', 'Granada', 418), 
    ('Madrid', 'San Sebastián', 452),
    
    ('Barcelona', 'Valencia', 350), 
    ('Barcelona', 'Zaragoza', 305),
    ('Barcelona', 'Alicante', 520),
    
    ('Valencia', 'Seville', 650),
    ('Valencia', 'Bilbao', 620),
    ('Valencia', 'Alicante', 170),
    
    ('Seville', 'Málaga', 205),
    ('Seville', 'Córdoba', 140),
    ('Seville', 'Cádiz', 121),
    
    ('Bilbao', 'San Sebastián', 100),
    
    ('Córdoba', 'Granada', 130),
    
    ('Málaga', 'Granada', 135)
]

# geographical coordinates
geo_pos = {
    'Madrid': (-3.7038, 40.4168), 
    'Barcelona': (2.1734, 41.3851),
    'Valencia': (-0.3763, 39.4699),
    'Seville': (-5.9867, 37.3887),
    'Bilbao': (-2.9350, 43.2630),
    'Zaragoza': (-0.8891, 41.6488), 
    'Córdoba': (-4.7794, 37.9882), 
    'Granada': (-3.5986, 37.1774), 
    'San Sebastián': (-1.9812, 43.7),
    'Alicante': (-0.4810, 38.3452),
    'Málaga': (-4.4215, 36.7213),
    'Cádiz': (-6.2928, 36.5298)
}


# Ensure all cities are present, even if they have no connections in the edge list
all_cities = set()
for u, v, w in edge_list:
    all_cities.add(u)
    all_cities.add(v)

G = nx.Graph()

G.add_weighted_edges_from(edge_list)

# visualisation of the graph
#pos = nx.spring_layout(G, seed=110)
nx.draw(G, geo_pos, with_labels=True)
labels=nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G,geo_pos,edge_labels=labels)

plt.title("Spanish cities (geographical layout)")
plt.gca().set_aspect('equal', adjustable='box') 
plt.axis('off')
plt.show()

# examining elements of graph
print(Fore.GREEN + "Nodes (cities) of the graph:")
print(Fore.WHITE+ f"{list(G.nodes)}")
print(Fore.YELLOW+"---------------------------------")
print(Fore.GREEN + "Edges (connections) of the graph:")
for edge in list(G.edges):
    print(Fore.WHITE + f"{edge}")
print(Fore.YELLOW+"---------------------------------")
print(Fore.GREEN+f"Number of nodes (cities) in graph: {G.number_of_nodes()}")
print(Fore.YELLOW+"---------------------------------")
print(Fore.GREEN+f"Number of edges (connections) in graph: {G.number_of_edges()}")
print(Fore.YELLOW+"---------------------------------")
print(Fore.GREEN+"Neighbor cities of Madrid:")
print(Fore.WHITE + f"{G["Madrid"]}")
print(Fore.YELLOW+"---------------------------------")

print(Fore.GREEN+"Degrees of the nodes(cities):")
for city in G.nodes:
    print(Fore.WHITE + f"{city}: {G.degree[city]} neighbours")
print(Fore.YELLOW+"---------------------------------")

print(Fore.GREEN+"Degree centrality:")
for item in nx.degree_centrality(G).items():
    print(Fore.WHITE+f"{item}")
print(Fore.YELLOW+"---------------------------------")

print(Fore.GREEN+"Closeness centrality:")
for item in nx.closeness_centrality(G).items():
    print(Fore.WHITE+f"{item}")
print(Fore.YELLOW+"---------------------------------")

print(Fore.GREEN+"Betweenness centrality:")
for item in nx.betweenness_centrality(G).items():
    print(Fore.WHITE+f"{item}")
print(Fore.YELLOW+"---------------------------------")


# applying algoritms DFS and BFS 
print(Fore.GREEN+"DFS algoritm:")
dfs_tree = nx.dfs_tree(G, source='Bilbao')
print(Fore.WHITE+f"{dfs_tree.in_edges()}")
print(Fore.YELLOW+"---------------------------------")

print(Fore.GREEN+"BFS algoritm:")
bfs_tree = nx.bfs_tree(G, source='Bilbao')
print(Fore.WHITE+f"{list(bfs_tree.edges())}")
print(Fore.YELLOW+"---------------------------------")


# Dijkstra algoritm to find the shortest path from Bilbao to Cadiz
def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in list(graph.nodes)}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight['weight']

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

print(Fore.GREEN+"Algoritm Deijkstra to find the shortest paths to all cities (in km):")
for city in list(G.nodes()):
    print(Fore.BLUE+f"Shortest paths from {city}:")
    print(Fore.WHITE+f"{dijkstra(G, city)}")
    print("\n")
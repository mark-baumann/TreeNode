from binarytree import Node
import heapq

def dijkstra(graph, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def reconstruct_path(prev, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = prev.get(current)
        if current is None:
            return []
    path.append(start)
    return path[::-1]

def build_binary_path_tree(path):
    """
    Baut einen binären Baum aus einer Pfadliste.
    Der linke Kindknoten ist immer der nächste Pfadknoten, rechter Knoten bleibt leer.
    """
    if not path:
        return None
    root = Node(path[0])
    current = root
    for value in path[1:]:
        new_node = Node(value)
        current.left = new_node  # Linkskind zeigt auf nächsten Knoten im Pfad
        current = new_node
    return root

# Beispielgraph
graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
    'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
    'E': [('C', 8), ('D', 3)],
    'F': [('D', 6)]
}

# Dijkstra starten
start_node = 'A'
distances, prev = dijkstra(graph, start_node)

# Ausgabe der Distanzen
print(f"Kürzeste Distanzen von '{start_node}':")
for node in sorted(graph.keys()):
    dist = distances[node]
    print(f"  {node}: {dist if dist != float('inf') else 'unreachable'}")

# Kürzesten Pfad zu einem Zielknoten visualisieren
zielknoten = 'F'
pfad = reconstruct_path(prev, start_node, zielknoten)

print(f"\nPfad von {start_node} nach {zielknoten}: {' → '.join(pfad) if pfad else 'kein Pfad'}")

# Binärbaum bauen und anzeigen
baum = build_binary_path_tree(pfad)
print("\nVisualisierung des Pfads als binärer Baum (nur linker Ast):")
print(baum)

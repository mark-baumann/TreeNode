from binarytree import Node
import heapq

# ------------------------
# Binärbaum manuell erstellen
# ------------------------
node11 = Node(11)
node10 = Node(10, None, node11)
node9 = Node(9, None, node10)
node8 = Node(8)
node7 = Node(7)
node6 = Node(6, node7, node8)
node5 = Node(5)
node4 = Node(4, node9, None)
node3 = Node(3, None, node4)
node2 = Node(2, node5, node6)
root = Node(1, node2, node3)

# ------------------------
# Ausgabe des Binärbaums
# ------------------------
print("Binärbaum-Struktur:\n")
print(root)
print("\n")

# ------------------------
# Adjazenzliste mit Gewicht = 1 für jede Kante
# ------------------------
def build_graph(node):
    graph = {}

    def add_edge(u, v):
        if u not in graph:
            graph[u] = []
        graph[u].append((v, 1))

    def helper(n):
        if n is None:
            return
        if n.left:
            add_edge(n.value, n.left.value)
            add_edge(n.left.value, n.value)
            helper(n.left)
        if n.right:
            add_edge(n.value, n.right.value)
            add_edge(n.right.value, n.value)
            helper(n.right)
    helper(node)
    return graph

graph = build_graph(root)

# ------------------------
# Dijkstra-Algorithmus
# ------------------------
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    previous_nodes = {}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes

# ------------------------
# Pfadrekonstruktion
# ------------------------
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

# ------------------------
# Ausführung
# ------------------------
start_node = root.value
distances, prev = dijkstra(graph, start_node)

print(f"Kürzeste Distanzen von Knoten {start_node}:")
for node in sorted(graph):
    print(f"  {node}: {distances[node]}")

print("\nKürzeste Pfade von Wurzelknoten:")
for target in sorted(graph):
    if target == start_node:
        continue
    path = reconstruct_path(prev, start_node, target)
    print(f"  {start_node} → {target}: {' → '.join(map(str, path))}")

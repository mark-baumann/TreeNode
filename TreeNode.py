from binarytree import Node

# Baum manuell bauen
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

# Baum ausgeben
print("Binärbaum:")
print(root)
print("\n")

# Traversierungen
def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.value)
    inorder(node.right, result)

def preorder(node, result):
    if node is None:
        return
    result.append(node.value)
    preorder(node.left, result)
    preorder(node.right, result)

def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.value)

# Adjazenzliste (als Dict): node -> [left, right] wenn vorhanden
def adjacency_list(node):
    adj = {}
    def helper(n):
        if n is None:
            return
        neighbors = []
        if n.left:
            neighbors.append(n.left.value)
        if n.right:
            neighbors.append(n.right.value)
        adj[n.value] = neighbors
        helper(n.left)
        helper(n.right)
    helper(node)
    return adj

# Adjazenzmatrix: Liste aller Knoten, dann Matrix NxN mit 1/0 für Kanten
def adjacency_matrix(adj_list):
    nodes = sorted(adj_list.keys())  # sortiert nach Wert (Nummern/ Buchstaben)
    index = {node: i for i, node in enumerate(nodes)}
    size = len(nodes)
    matrix = [[0]*size for _ in range(size)]
    for u, neighbors in adj_list.items():
        for v in neighbors:
            matrix[index[u]][index[v]] = 1
    return nodes, matrix

# Ergebnisse sammeln
inorder_result = []
preorder_result = []
postorder_result = []

inorder(root, inorder_result)
preorder(root, preorder_result)
postorder(root, postorder_result)

print("Inorder Traversierung:", inorder_result)
print("Preorder Traversierung:", preorder_result)
print("Postorder Traversierung:", postorder_result)

# Adjazenzliste ausgeben
adj_list = adjacency_list(root)
print("\nAdjazenzliste:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")

# Adjazenzmatrix ausgeben
nodes, matrix = adjacency_matrix(adj_list)
print("\nAdjazenzmatrix:")
print("   " + " ".join(str(n) for n in nodes))
for i, row in enumerate(matrix):
    print(f"{nodes[i]:2} " + " ".join(str(x) for x in row))

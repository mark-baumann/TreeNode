import networkx as nx
import matplotlib.pyplot as plt

# Beispiel-Baum als Dictionary: {Node: (Left, Right)}
tree = {
    'A': ('B', 'C'),
    'B': (None, None),
    'C': ('D', 'E'),
    'D': (None, None),
    'E': (None, None)
}

def build_graph_from_tree(tree, node, G):
    left, right = tree.get(node, (None, None))
    if left:
        G.add_edge(node, left)
        build_graph_from_tree(tree, left, G)
    if right:
        G.add_edge(node, right)
        build_graph_from_tree(tree, right, G)

def hierarchy_pos(G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
    """
    Berechnet Positionen für eine Top-Down Baum-Visualisierung.
    Quelle: https://stackoverflow.com/a/29597209/1066234
    """
    def _hierarchy_pos(G, root, leftmost, width, vert_gap, vert_loc, pos, parent=None):
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = leftmost - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, nextx, dx, vert_gap, vert_loc - vert_gap, pos, root)
        pos[root] = (leftmost, vert_loc)
        return pos

    return _hierarchy_pos(G, root, xcenter, width, vert_gap, vert_loc, {})

def visualize_tree(tree, root='A'):
    G = nx.DiGraph()
    build_graph_from_tree(tree, root, G)

    pos = hierarchy_pos(G, root)
    nx.draw(G, pos, with_labels=True, arrows=False, node_size=2000, node_color="lightblue", font_size=14)
    plt.title("Binärbaum (Top-Down mit Root)")
    plt.show()
    return G

def inorder(tree, node, result):
    if node is None:
        return
    left, right = tree.get(node, (None, None))
    inorder(tree, left, result)
    result.append(node)
    inorder(tree, right, result)

def preorder(tree, node, result):
    if node is None:
        return
    result.append(node)
    left, right = tree.get(node, (None, None))
    preorder(tree, left, result)
    preorder(tree, right, result)

def postorder(tree, node, result):
    if node is None:
        return
    left, right = tree.get(node, (None, None))
    postorder(tree, left, result)
    postorder(tree, right, result)
    result.append(node)

def adjacency_list(G):
    adj_list = {node: list(G.neighbors(node)) for node in G.nodes()}
    return adj_list

def adjacency_matrix(G):
    nodes = list(G.nodes())
    index = {node: i for i, node in enumerate(nodes)}
    size = len(nodes)
    matrix = [[0]*size for _ in range(size)]
    for u, v in G.edges():
        i, j = index[u], index[v]
        matrix[i][j] = 1
    return nodes, matrix

# ---- Hauptprogramm ----
root = 'A'

# Baum visualisieren und Graph zurückbekommen
G = visualize_tree(tree, root)

# Traversierungen berechnen
inorder_result = []
preorder_result = []
postorder_result = []

inorder(tree, root, inorder_result)
preorder(tree, root, preorder_result)
postorder(tree, root, postorder_result)

print("Inorder Traversierung:", inorder_result)
print("Preorder Traversierung:", preorder_result)
print("Postorder Traversierung:", postorder_result)

# Adjazenzliste ausgeben
adj_list = adjacency_list(G)
print("\nAdjazenzliste:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")

# Adjazenzmatrix ausgeben
nodes, matrix = adjacency_matrix(G)
print("\nAdjazenzmatrix:")
print("  " + " ".join(nodes))
for i, row in enumerate(matrix):
    print(nodes[i], " ".join(str(x) for x in row))

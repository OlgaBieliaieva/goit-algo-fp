import uuid
import networkx as nx
import matplotlib.pyplot as plt
import queue

def generate_color(index, total):
    ratio = index / total
    r = int(18 + ratio * (255 - 18))
    g = int(54 + ratio * (255 - 54))
    b = int(122 + ratio * (255 - 122))
    return f'#{r:02X}{g:02X}{b:02X}'

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (x - 1 / 2 ** layer, y - 1)
            add_edges(graph, node.left, pos, x - 1 / 2 ** layer, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (x + 1 / 2 ** layer, y - 1)
            add_edges(graph, node.right, pos, x + 1 / 2 ** layer, y - 1, layer + 1)
    return graph

def visualize_traversal(tree_root, order):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    total_nodes = len(order)
    colors = {}
    for index, node in enumerate(order):
        colors[node] = generate_color(index, total_nodes)
    
    node_colors = [colors.get(node[0], "#AAAAAA") for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def bfs(root):
    q = queue.Queue()
    q.put(root)
    order = []
    while not q.empty():
        node = q.get()
        order.append(node.id)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return order

def dfs(root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node.id)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходу в ширину
visualize_traversal(root, bfs(root))
# Візуалізація обходу в глибину
visualize_traversal(root, dfs(root))

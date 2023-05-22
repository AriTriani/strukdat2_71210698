class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, parent, child):
        if not self.root:
            self.root = parent
        parent.children.append(child)

    def sums(self, node):
        if not node:
            return 0
        total = node.data
        for child in node.children:
            total += self.sums(child)
        return total

    def sibling(self, node):
        if not node:
            return 0
        total = 0
        for child in node.children:
            total += child.data
        return total

# Membangun struktur tree seperti yang diberikan
t = Tree()

val200 = Node(200)
val23 = Node(23)
val11 = Node(11)
val13 = Node(13)
val57 = Node(57)
val32 = Node(32)
val42 = Node(42)
val51 = Node(51)
val71 = Node(71)
val12 = Node(12)
val15 = Node(15)
val33 = Node(33)
val8 = Node(8)

t.add_node(val200, val23)
t.add_node(val200, val11)
t.add_node(val23, val13)
t.add_node(val23, val57)
t.add_node(val23, val32)
t.add_node(val11, val42)
t.add_node(val11, val51)
t.add_node(val11, val71)
t.add_node(val32, val12)
t.add_node(val32, val15)
t.add_node(val15, val33)
t.add_node(val15, val8)

# Testcase 1
print(f"Total value of node {val200.data} and all of its descendants = {t.sums(val200)}")

# Testcase 2
print(f"Total value of all siblings on node {val33.data} = {t.sibling(val33)}")



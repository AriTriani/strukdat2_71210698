class Graph:
    def __init__(self):
        self._data = {}

    def addVertex(self, vertex):
        if vertex not in self._data:
            self._data[vertex] = set()

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self._data and vertex2 in self._data:
            self._data[vertex1].add(vertex2)
            self._data[vertex2].add(vertex1)

    def vertex(self):
        print("Seluruh Node =", end=" ")
        for vertex in self._data:
            print(vertex, end=" ")
        print()

    def edge(self):
        print("Seluruh Edge =", end=" ")
        edges = set()
        for vertex in self._data:
            for neighbor in self._data[vertex]:
                edge = tuple(sorted([vertex, neighbor]))
                edges.add(edge)
        for edge in edges:
            print("".join(edge), end=" ")
        print()

    def bfs(self, node):
        print("Traversing BFS =", end=" ")
        visited = set()
        queue = [node]
        visited.add(node)
        while queue:
            current = queue.pop(0)
            print(current, end=" ")
            for neighbor in self._data[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()


# Main program
graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')
graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('c', 'e')
graph.addEdge('e', 'g')
graph.addEdge('f', 'g')

graph.vertex()
graph.edge()
graph.bfs("a")

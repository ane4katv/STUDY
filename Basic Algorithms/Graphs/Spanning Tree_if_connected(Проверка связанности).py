
class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, nbr, cost=0):
        self.neighbors.append((nbr, cost))


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, key):
        self.graph[key] = Vertex(key)

    def connect_vertices(self, start, end, cost=0):
        if start not in self.graph:
            self.add_vertex(start)

        if end not in self.graph:
            self.add_vertex(end)

        self.graph[start].add_neighbor(self.graph[end].value, cost)

    def __str__(self):
        printed = dict()
        for k, v in self.graph.items():
            printed[k] = v.neighbors

        return str(printed)

    def if_connected(self, root):
        stack = [root]

        while stack:
            popped = stack.pop()

            self.graph[popped].visited = True

            for value in self.graph[popped].neighbors:
                stack.append(value[0])

        for key in self.graph:

            if self.graph[key].visited is False:
                return False

        return True


g = Graph()

g.connect_vertices("A", "B", 7)
g.connect_vertices("B", "C", 3)
g.connect_vertices("C", "D", 2)
# g.connect_vertices("E", "F", 8)

print(g)
print(g.if_connected("A"))



class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, nbr, capacity, rev_capacity):
        self.neighbors.append((nbr, capacity, rev_capacity))


class Graph:
    def __init__(self):
        self.graph = dict()

    def add_vertex(self, value):
        self.graph[value] = Vertex(value)

    def edges(self, start, end, capacity, rev_capacity):
        if start not in self.graph:
            self.add_vertex(start)
        if end not in self.graph:
            self.add_vertex(end)

        self.graph[start].add_neighbor(self.graph[end].value, capacity, rev_capacity)

    def __str__(self):
        graph = dict()
        for i in self.graph:
            a = self.graph[i].neighbors

            graph[i] = [i for i in a]

        return str(graph)

    def max_flow(self, source, sink):
        residual_graph = self.graph
        current = source
        queue = []
        max_flow = 0
        visited = set()











g = Graph()


g.edges("A", "B", 3, 0)
g.edges("A", "D", 3, 0)
g.edges("B", "C", 4, 0)
g.edges("B", "E", 1, 0)
g.edges("C", "A", 3, 0)
g.edges("C", "D", 1, 0)
g.edges("C", "E", 2, 0)
g.edges("D", "E", 2, 0)
g.edges("D", "F", 6, 0)
g.edges("E", "G", 1, 0)
g.edges("F", "G", 9, 0)


print(g)





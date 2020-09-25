# NotWeighted, NotDirected Graph

# Для направленного графа все будет то же самое как для ненаправленного кроме
# connect only start to end (line 33), а не в обе стороны?



class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = set()

    def add_neighbor(self, nbr):
        self.neighbors.add(nbr)

    def __str__(self):
        return f'{self.value}: {sorted([_.key for _ in self.neighbors])}'


class NotWeighted:
    def __init__(self):
        self.not_weighted = dict()

    def add_vertex(self, key):
        self.not_weighted[key] = Vertex(key)

    def connect_vertices(self, start, end):
        if start not in self.not_weighted:
            self.add_vertex(start)

        if end not in self.not_weighted:
            self.add_vertex(end)

        # connect start to end AND end to start (for not directed graph)
        self.not_weighted[start].add_neighbor(self.not_weighted[end])
        self.not_weighted[end].add_neighbor(self.not_weighted[start])

    def __str__(self):
        graph = dict()
        for i in self.not_weighted:
            a = self.not_weighted[i].neighbors

            graph[i] = set([i.value for i in a])

        return str(graph)


if __name__ == "__main__":
    graph_1 = NotWeighted()

    graph_1.connect_vertices("A", "B")
    graph_1.connect_vertices("A", "C")
    graph_1.connect_vertices("B", "C")
    graph_1.connect_vertices("B", "E")
    graph_1.connect_vertices("C", "E")
    graph_1.connect_vertices("C", "F")

    print(graph_1)


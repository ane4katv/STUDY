# Weighted, NotDirected Graph

# Для направленного графа все будет то же самое как для ненаправленного кроме
# connect only start to end (line 33), а не в обе стороны?


class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = dict()

    def add_neighbor(self, nbr, weight):
        self.neighbors[nbr] = weight

    def __str__(self):
        return str(self.neighbors)


class Weighted:
    def __init__(self):
        self.weighted = dict()

    def add_vertex(self, key):
        self.weighted[key] = Vertex(key)

    def connect_vertices(self, start, end, cost=0):
        if start not in self.weighted:
            self.add_vertex(start)

        if end not in self.weighted:
            self.add_vertex(end)

        self.weighted[start].add_neighbor(self.weighted[end], cost)
        self.weighted[end].add_neighbor(self.weighted[start], cost)


    def __str__(self):
        dic = dict()
        for k, v in self.weighted.items():
            dic[k] = v.neighbors

        return str(dic)


if __name__ == "__main__":

    graph_1 = Weighted()
    graph_1.connect_vertices("A", "B", 5)
    graph_1.connect_vertices("A", "C", 10)
    graph_1.connect_vertices("B", "C", 15)
    graph_1.connect_vertices("B", "E", 6)
    graph_1.connect_vertices("C", "E", 3)
    graph_1.connect_vertices("C", "F", 8)

    print(graph_1)


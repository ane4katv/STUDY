from pprint import pprint


class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

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

    def shortest_paths(self):
        infinity = float('inf')
        distance = []

        for i in range(len(self.graph)):
            distance.append([infinity for _ in range(len(self.graph))])
            distance[i][i] = 0

        coordinates = []
        for k, v in self.graph.items():
            for value in v.neighbors:
                coordinates.append((k-1, value[0]-1, value[1]))

        for coordinate in coordinates:
            distance[coordinate[0]][coordinate[1]] = coordinate[2]

        print(distance)


g = Graph()
for i in range(1, 4):
    g.add_vertex(i)

g.connect_vertices(1, 4, 7)
g.connect_vertices(1, 2, 3)

g.connect_vertices(2, 3, 2)
g.connect_vertices(2, 1, 8)

g.connect_vertices(3, 1, 5)
g.connect_vertices(3, 4, 1)

g.connect_vertices(4, 1, 2)

print(g)

g.shortest_paths()

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

    def distance_matrix(self):
        infinity = float('inf')
        distance = []

        for i in range(len(self.graph)):
            distance.append([infinity for _ in range(len(self.graph))])
            distance[i][i] = 0

        coordinates = []
        for k, v in self.graph.items():
            for value in v.neighbors:
                coordinates.append((k - 1, value[0] - 1, value[1]))

        for coordinate in coordinates:
            distance[coordinate[0]][coordinate[1]] = coordinate[2]

        return distance

    def via_matrix(self):
        via = self.distance_matrix()

        for i in range(len(via)):
            for j in range(len(via)):
                if via[i][j] == float('inf'):
                    via[i][j] = -1
                else:
                    via[i][j] = j + 1
                via[i][i] = 0

        return via

    def shortest_distances(self):
        size = len(self.graph)
        distance = self.distance_matrix()
        via = self.via_matrix()

        for via_node in range(size):
            for from_node in range(size):
                for to_node in range(size):

                    new_distance = distance[from_node][via_node] + \
                                   distance[via_node][to_node]


                    if new_distance < distance[from_node][to_node]:
                        distance[from_node][to_node] = new_distance
                        via[from_node][to_node] = via_node + 1

        return distance, via

    def shortest_path(self, start, end, path=[]):
        via = self.shortest_distances()[1]

        if via[start-1][end-1] == end:
            if start not in path:
                path.append(start)
            if end not in path:
                path.append(end)
        else:
            inside = via[start - 1][end - 1]
            self.shortest_path(start, inside, path)
            self.shortest_path(inside, end, path)

        return path


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

print(g.shortest_distances())
print(g.shortest_path(4, 2))

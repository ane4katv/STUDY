
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

        self.graph[start].add_neighbor(self.graph[end], cost)

    def __str__(self):
        printed = dict()
        for k, v in self.graph.items():
            printed[k] = [v[0].value for v in v.neighbors]

        return str(printed)

    def connected_paths(self):
        stack = []
        count_visited = 0
        connected_lists = []

        while count_visited < len(self.graph):
            for vertex in self.graph:
                if self.graph[vertex].visited is False:
                    stack.append(self.graph[vertex])
                    count_visited += 1
                    self.graph[vertex].visited = True

                    new_list = [vertex]

                    while stack:
                        popped = stack.pop()
                        for neighbor in popped.neighbors:
                            if neighbor[0].visited is False:
                                neighbor[0].visited = True
                                count_visited += 1
                                stack.append(neighbor[0])

                            new_list.append(neighbor[0].value)

                    connected_lists.append(new_list)

        return connected_lists




g = Graph()

g.connect_vertices("A", "B", 7)
g.connect_vertices("A", "G", 15)
g.connect_vertices("B", "C", 3)
g.connect_vertices("C", "D", 2)
g.connect_vertices("E", "F", 8)

print(g)
print(g.connected_paths())


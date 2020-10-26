
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

    def connected_paths(self, root):
        stack = [root]
        count_visited = 0
        connected_lists = []

        while count_visited < len(self.graph):

            # add vertex to stack (how?)
            # vertex.visited = True
            # count_visited += 1


            while stack:
                new_list = []
                popped = stack.pop()

                for i in self.graph[popped]:
                    if self.graph[popped][0].visited is False:
                        self.graph[popped][0].visited = True
                        count_visited += 1

                    stack.append(i[0])

                connected_lists.append(new_list)




g = Graph()

g.connect_vertices("A", "B", 7)
g.connect_vertices("A", "G", 15)
g.connect_vertices("B", "C", 3)
g.connect_vertices("C", "D", 2)
g.connect_vertices("E", "F", 8)

print(g)
print(g.connected_paths("A"))


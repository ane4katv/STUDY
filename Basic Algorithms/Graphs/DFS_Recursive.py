from collections import deque


class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def add_neighbor(self, nbr, cost):
        self.neighbors[nbr] = cost

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
        printed = {}
        for k, v in self.graph.items():
            printed[k] = v.neighbors

        return str(printed)

    def dfs_recursive(self, vertex, path):
        path.append(vertex)

        for neighbor in self.graph[vertex].neighbors:
            if neighbor not in path:
                path = self.dfs_recursive(neighbor, path)

        return path


graph_1 = Graph()

graph_1.connect_vertices("A", "B", 10)
graph_1.connect_vertices("A", "C", 13)
# graph_1.connect_vertices("B", "C", 1)
graph_1.connect_vertices("B", "D", 2)
graph_1.connect_vertices("C", "E", 2)
# graph_1.connect_vertices("C", "B", 4)
# graph_1.connect_vertices("D", "E", 9)
# graph_1.connect_vertices("D", "E", 7)
graph_1.connect_vertices("D", "S", 7)
graph_1.connect_vertices("S", "W", 5)
graph_1.add_vertex("F")

print(graph_1)

print(graph_1.dfs_recursive('A', []))

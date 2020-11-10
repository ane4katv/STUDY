from collections import OrderedDict


class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, nbr, size):
        self.neighbors.append([nbr, size])


class Graph:
    def __init__(self):
        self.graph = dict()

    def add_vertex(self, value):
        self.graph[value] = Vertex(value)

    def edges(self, start, end, size):
        if start not in self.graph:
            self.add_vertex(start)
        if end not in self.graph:
            self.add_vertex(end)

        self.graph[start].add_neighbor(self.graph[end].value, size)
        self.graph[end].add_neighbor(self.graph[start].value, size)

    def prim(self, vertex):
        min_edges = []
        queue = [vertex]
        visited = [vertex]

        while queue:
            edges = {}
            popped = queue.pop(0)

            for end, weight in self.graph[popped].neighbors:
                if end not in visited:
                    edges[weight] = (popped, end)

            if len(edges) > 0:
                min_edge = sorted(edges.items())[0][1]
                if min_edge not in min_edges and min_edge[::-1] not in min_edges:
                    min_edges.append(min_edge)

                queue.append(min_edge[1])
                visited.append(min_edge[1])
            else:
                if len(visited) == len(edges):
                    return min_edges
                else:
                    for i in self.graph:
                        if i not in visited:
                            sorted_i = sorted(self.graph[i].neighbors, key=lambda x: x[1])
                            new_min_edge = (i, sorted_i[0][0])

                            if new_min_edge not in min_edges and new_min_edge[::-1] not in min_edges:
                                min_edges.append(new_min_edge)
        return min_edges


    def __str__(self):
        graph = dict()
        for i in self.graph:
            graph[i] = [i for i in self.graph[i].neighbors]

        return str(graph)


g = Graph()

g.edges("A", "B", 8)
g.edges("A", "E", 5)
g.edges("A", "H", 6)
g.edges("A", "F", 1)
g.edges("B", "C", 4)
g.edges("F", "B", 6)
g.edges("C", "F", 2)
g.edges("C", "G", 7)
g.edges("G", "F", 9)
g.edges("F", "H", 5)
g.edges("H", "E", 3)

# print(g)
print(g.prim("A"))
# print(g.min_edge())

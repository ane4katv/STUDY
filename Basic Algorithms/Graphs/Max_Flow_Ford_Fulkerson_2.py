
class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, nbr, capacity, rev_capacity, visited=False):
        self.neighbors.append([nbr, capacity, rev_capacity, visited])


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

        self.graph[start].add_neighbor(self.graph[end].value, capacity, rev_capacity, False)

    def __str__(self):
        graph = dict()
        for i in self.graph:
            graph[i] = [i for i in self.graph[i].neighbors]

        return str(graph)

    def max_flow(self, source, sink):
        max_flow = 0
        new_graph = self.graph
        path = [source]

        while path:
            path = self.path_finder(new_graph, source, sink)
            capacity = self.capacity(new_graph, path)
            max_flow += capacity[1]
            new_graph = capacity[0]

        return max_flow

    def path_finder(self, graph, source, sink):
        queue = [source]
        visited = []
        parents = dict()
        current = -1

        while queue:
            popped = queue.pop(0)

            if popped not in visited:
                visited.append(popped)
                current = popped

                for i in graph[popped].neighbors:
                    if i[3] is not True:
                        queue.append(i[0])
                        parents[i[0]] = current

        if current != sink:
            return []
        else:
            child = sink
            parent = parents[sink]
            path = []

            while parent != source:
                path.insert(0, [parent, child])
                child = parents[child]
                parent = parents[child]

            path.insert(0, [source, child])

        return path

    def capacity(self, graph, path):
        flow = []
        edges = []

        for start, end in path:
            for i in graph[start].neighbors:
                if i[0] == end:
                    flow.append(i[1])
                    edges.append([start, end, i[1], i[2], i[3]])

        capacity = 0

        if flow:
            capacity = min(flow)

        for start, end, value, flow, visited in edges:
            for j in graph[start].neighbors:

                if j[0] == end and j[1] == capacity:
                    j[3] = True
                else:
                    j[1] -= capacity

        return graph, capacity

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

# print(g)

print(g.max_flow("A","G"))








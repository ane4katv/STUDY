class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, nbr, capacity, rev_capacity):
        self.neighbors.append([nbr, capacity, rev_capacity])


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
            graph[i] = [i for i in self.graph[i].neighbors]

        return str(graph)

    def path_finder(self, source, sink, residual_graph):
        current = -1
        queue = [source]
        parents = dict()
        visited = set()

        while queue:
            popped = queue.pop(0)
            if popped not in visited:
                visited.add(popped)
                current = popped

                for i in residual_graph[popped].neighbors:
                    if i[0] not in visited and (i[1] > 0):
                        queue.append(i[0])
                        parents[i[0]] = current

        if current == sink:
            child = sink
            path = [sink]

            while child in parents:
                path.insert(0, parents[child])
                child = parents[child]

            return path
        else:
            return []

    def capacity(self, source, sink, graph):
        path = self.path_finder(source, sink, graph)
        flow = []

        for i in range(len(path)):
            for j in graph[path[i]].neighbors:
                if j[0] == path[i+1]:
                    flow.append(j[1])
        print(f'flow: {flow}')
        capacity = min(flow)

        return path, capacity

    def update_graph(self, source, sink, graph):
        path, capacity = self.capacity(source, sink, graph)
        print(f'path: {path}')
        print(f'capacity: {capacity}')
        for i in range(len(path)):
            for j in graph[path[i]].neighbors:
                if j[0] == path[i + 1]:
                    j[1] -= capacity
                    j[2] += capacity
        return path, capacity, graph

    def max_flow(self, source, sink):
        max_flow = 0
        new_graph = self.graph
        path = [source]

        while path:
            path, capacity, new_graph = self.update_graph(source, sink, new_graph)
            max_flow += capacity

        return max_flow


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
g.max_flow("A", "G")










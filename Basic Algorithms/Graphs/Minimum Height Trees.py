
from collections import deque


class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.index = -1

    def add_neighbor(self, nbr):
        self.neighbors.append(nbr)


class Graph:
    def __init__(self):
        self.graph = dict()

    def add_vertex(self, value):
        self.graph[value] = Vertex(value)

    def edges(self, start, end):
        self.graph[start].add_neighbor(self.graph[end])
        self.graph[end].add_neighbor(self.graph[start])

    def __str__(self):
        graph = dict()
        for i in self.graph:
            a = self.graph[i].neighbors

            graph[i] = [i.value for i in a]

        return str(graph)

    def bfs_farthest(self, value):
        queue = deque([value])
        visited = []
        parent = dict()

        while queue:
            popped = queue.popleft()

            if popped not in visited:
                visited.append(popped)

                for value in self.graph[popped].neighbors:
                    queue.append(value.value)
                    if value.value not in visited:
                        parent[value.value] = popped

        return visited[-1], parent

    def diameter_middle(self, value):
        first = self.bfs_farthest(value)[0]
        second = self.bfs_farthest(first)[0]

        parents = self.bfs_farthest(first)[1]
        path = []
        queue = [second]

        while queue:
            popped = queue.pop()
            path.insert(0, popped)
            for k, v in parents.items():
                if k == popped:
                    queue.append(v)

        middle = []
        size_halved = int(len(path)/2)
        if size_halved % 2 == 0:
            middle.append(path[size_halved])
        else:
            middle.append(path[size_halved - 1])
            middle.append(path[size_halved])

        return middle


g = Graph()
for i in range(10):
    g.add_vertex(i)

g.edges(0,1)
g.edges(1,2)
g.edges(1,6)
g.edges(2,3)
g.edges(2,4)
g.edges(2,9)
g.edges(4,5)
g.edges(6,8)
g.edges(6,7)

print(g.diameter_middle(0))




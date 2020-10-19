
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

    def farthest(self, value):
        queue = deque([value])
        visited = []
        parent = dict()

        while queue:
            popped = queue.popleft()

            if popped not in visited:
                visited.append(popped)

                for value in self.graph[popped].neighbors:
                    queue.append(value.value)
                    parent[value.value] = popped

        print(f'parent: {parent}')

        return visited[-1]

    def diameter(self, value):
        first = self.farthest(value)
        second = self.farthest(first)

        print(first, second)
        print("============")

        queue = deque([first])
        visited = []
        heights = dict()

        while queue:
            popped = queue.popleft()

            if popped not in visited:
                visited.append(popped)

                for value in self.graph[popped].neighbors:
                    if value.value not in visited:
                        queue.append(value.value)
                        value.index = popped

                        heights[popped] = value.index
                        print(heights)


        # print([(value.value, value.index) for value in self.graph])


        return visited






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
# g.edges(16,17)

print(g)
g.diameter(5)




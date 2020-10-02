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

    def bfs(self, root):
        queue = deque([root])
        visited = []

        while queue:
            popped = queue.popleft()

            if popped not in visited:
                visited.append(popped)

                for value in self.graph[popped].neighbors:
                    queue.append(value)

        for key in self.graph:  # for disconnected graph
            if self.graph[key].neighbors == {} and key not in visited:
                visited.append(key)

        return visited

    def dfs(self, root):
        stack = [root]
        visited = []

        while stack:
            popped = stack.pop()

            if popped not in visited:
                visited.append(popped)

                for value in self.graph[popped].neighbors:
                    stack.append(value)

        for key in self.graph:  # for disconnected graph
            if self.graph[key].neighbors == {} and key not in visited:
                visited.append(key)

        return visited


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

# print(graph_1.bfs("A"))
print(graph_1.dfs("A"))

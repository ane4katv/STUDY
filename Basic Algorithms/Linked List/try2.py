class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = []

        for i in range(size):
            self.adj_matrix.append([j for j in range(size)])

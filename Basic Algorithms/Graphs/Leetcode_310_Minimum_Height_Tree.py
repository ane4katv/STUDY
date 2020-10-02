class Graph:

    def __init__(self, n):
        self.n = n
        self.adj = dict((i, []) for i in range(n))
        self.degree = list()
        for i in range(n):
            self.degree.append(0)

    def add_edge(self, start, end):
        self.adj[start].append(end)  # Adds start to end's list
        self.adj[end].append(start)  # Adds end to start's list
        self.degree[start] += 1      # increment degree of start by 1
        self.degree[end] += 1      # increment degree of end by 1

        print(start, end, self.degree)

    def min_height_root(self):
        queue = []

        # First enqueue all leaf nodes in queue
        for i in range(self.n):
            if self.degree[i] <= 1:
                queue.append(i)
                print(queue)


        # loop until total vertex remains less than 2
        while self.n > 2:
            queue_size = len(queue)
            self.n -= queue_size
            for i in range(queue_size):
                popped = queue.pop(0)

                # for each neighbour, decrease its degree and
                # if it become leaf, insert into queue
                for j in self.adj[popped]:
                    self.degree[j] -= 1
                    if self.degree[j] == 1:
                        queue.append(j)

        #  Copying the result from queue to result vector
        res = list()
        while len(queue) > 0:
            res.append(queue.pop(0))

        return res


g = Graph(6)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(4, 3)
g.add_edge(5, 4)

print(g.min_height_root())
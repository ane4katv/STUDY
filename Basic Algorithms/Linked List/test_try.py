N = 6 # len of the graph
parents = []
infinite = float('inf')


def bfs(residual_graph, source, sink, parents):
    queue = []
    visited = []

    for x in range(0, N):
        visited.append(0)

    queue.append(source)
    visited[source] = True
    parents[source] = -1

    while queue: # originally while not len(queue) == 0 ?!
        u = queue.pop(0)
        for v in range(0, N):
            if visited[v] is False and residual_graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parents[v] = u

    if visited[sink]:
        return True
    else:
        return False

def ford_fulkerson(g, source, sink):
    u = 0
    v = 0

    residual_graph = g
    max_flow = 0

    while bfs(residual_graph, source, sink, parents):
        path_flow = infinite
        v = sink

        while v != source:
            u = parents[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = parents[v]

        v = sink

        while v != source:
            u = parents[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow

            v = parents[v]

        max_flow += path_flow

    return max_flow()


def main():
    graph = \
    [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4]
    ]

    for x in range(0, N):
        parents.append(0)

    print(f'max possible flow is {ford_fulkerson(graph, 0, N-1)}')

if __name__ == '__main__':
    main()








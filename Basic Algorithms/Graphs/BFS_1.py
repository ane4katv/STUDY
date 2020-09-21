from collections import deque


def bfs(graph, root):
    queue = deque()
    queue.append(root)
    visited = []

    while queue:
        popped = queue.popleft()
        if popped not in visited:
            visited.append(popped)
            for value in graph[popped]:
                queue.append(value)

    for key in graph:   # for disconnected graph
        if graph.get(key) == {} and key not in visited:
            visited.append(key)

    print(visited)


graph1 = {0: {1, 2, 3}, 1: {0, 2}, 2: {1, 4}, 3: {}, 4: {}, 5: {}}
bfs(graph1, list(graph1)[0])

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

    print(visited)


graph1 = {0: {1, 2, 3}, 1: {0, 2}, 2: {1, 4}, 3: {}, 4: {}}
bfs(graph1, list(graph1)[0])

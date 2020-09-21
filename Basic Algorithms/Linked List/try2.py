from collections import deque


def bfs(graph, root):
    stack = [root]
    visited = []

    while stack:
        popped = stack.pop()
        if popped not in visited:
            visited.append(popped)
            for value in graph[popped]:
                stack.append(value)

    print(visited)


graph1 = {0: {1, 2, 3}, 1: {0, 2}, 2: {1, 4}, 3: {}, 4: {}}
bfs(graph1, list(graph1)[0])

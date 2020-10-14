"""

- Center of the tree: MHT (Minimum Height Tree) root -  node, that minimizes remoteness
We can have 1 (when length is odd) or at most 2 centers (when length is even)

- Degree of the node is the number of its neighbors

- Leaf has degree of 1 in undirected graph (when it's only connected to its parent)

- If we find longest path, we can take the middle of it (1 or 2 nodes)

Greedy approach:

1. select any node x
2. Preform DFS or BFS
3. Find node y with the highest r(x) (remoteness, longest distance from x)
4. Let y be the new root
5. Preform DFS or BFS for y
6. Find node z with the highest r(y) (longest distance from y)
7. The path y to z will be the longest path
8. Return the middle of found longest path (1 or 2 nodes)
"""
import collections


def find_min_height_trees(n, edges):
    if n == 1:
        return [0]

    adj = collections.defaultdict(set) # adj = [set() for _ in range(n)]

    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    def max_path(node, visited):  # DFS
        visited.add(node)
        paths = [max_path(neighbor, visited) for neighbor in adj[node] if neighbor not in visited]
        path = max(paths or [[]], key=len)
        path.append(node)  # y at path[0]
        return path


    x = 0  # step 1
    path = max_path(x, set())  # steps 2, 3
    y = path[0]  # step 4
    path = max_path(y, set())  # steps 5, 6
    # z = path[0]
    size = len(path)
    return path[(size-1)//2:size//2+1]




num = 4
input_edges = [[1, 0], [1, 2], [1, 3]]

print(find_min_height_trees(num, input_edges))
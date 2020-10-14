"""https://leetcode.com/problems/minimum-height-trees/discuss/479559/Python3-O(n)-with-explanation

- Remoteness R(V): Distance from root (V) to furthest node, its height

- Center of the tree: MHT (Minimum Height Tree) root -  node, that minimizes remoteness
We can have 1 (when length is odd) or at most 2 centers (when length is even)

- Degree of the node is the number of its neighbors

- Leaf has degree of 1 in undirected graph (when it's only connected to its parent)

- Path Graph (Linear Graph): tree with 2 or more vertices that do not have branches.
  Each vertex has degree 1 or 2(max)
  Paths are  important as subgraphs (for divide on conquer algorithms)


  a < - pointer_1       a
  |                     |
  b                     b
  |                     |
  c                     c < - pointer_1
  |                     | < - pointer_2
  d                     d
  |                     |
  e < - pointer_2       e

move pointers toward each other till they meet
(at the same node (for odd length) or edge apart(for even length))

Generalize simpler solution:
1. put pointers on every leaf
2. move them simultaneously in
3. ?? whenever 2 pointers meet (at the same node or edge apart) -> keep only one of them
4. repeat 1-3 till we have 2 pointers left (at the same node or edge apart)
5. return the node(s) pointers pointing to

2 pointers that left shows node(s)in the longest path (that's why they left).
That's why we pick them as root (middle of the graph) to shorten total graph's height

BFS is suitable technique here, as it deals with graph level by level

Time complexity: O(n)
Space complexity: O(n)

"""

def find_min_height_trees(n, edges):

    if n == 1:
        return [0]

    adj = [set() for _ in range(n)]

    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    leaves = [node for node in range(n) if len(adj[node]) == 1]

    while n > 2:  # while it is not 1 or 2 (point(s) where we found the tree center)
        n -= len(leaves)
        new_leaves = []

        for leaf in leaves:
            j = adj[leaf].pop()
            adj[j].remove(leaf)

            if len(adj[j]) == 1:
                new_leaves.append(j)

        leaves = new_leaves

    return leaves

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

print(find_min_height_trees(n, edges))
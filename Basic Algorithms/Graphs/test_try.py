"""https://leetcode.com/problems/minimum-height-trees/discuss/479559/Python3-O(n)-with-explanation

- Remoteness R(V): Distance from root (V) to furthest node, its height

- Center of the tree: MHT (Minimum Height Tree) root -  node, that minimizes remotness
We can have most 2 centers (when length is even)

- Degree of the node is the number of its neighbors

- Leaf has degree of 1 in undirected graph (its only connected to its parent)

- Path graph/ linear graph: tree with 2 or more vertices that do not have branches
  each vertex has degree 1 or 2(max)
  Paths are  important in their role as subgraphs (for divide on conquer algorithms)


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
5. return the node pointers pointing to

2 pointers that left are in the longest path (that's why they left).
That's why we pick them as root (middle of the graph) to shorten total graph's height

BFS is suitable technique here, as it deals with graph level by level

Time complexity: O(n)
Space complexity: O(n)

"""

def find_min_height_trees(self, n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].append(adj[v])
        adj[v].append(adj[u])


"""

              1
           /      \
         2         3
        /  \     /   \
       4    5    6   7
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def size_recur(self, node):

        if not node:
            return 0

        l = self.size_recur(node.left)
        r = self.size_recur(node.right)

        return l + r + 1




tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.size_recur(tree.root))


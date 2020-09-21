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

    def height(self, node):
        if not node:
            return -1

        left = self.height(node.left)
        right = self.height(node.right)

        return max(left, right) + 1


tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.height(tree.root))


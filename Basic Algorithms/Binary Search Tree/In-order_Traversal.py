"""
In-order Traversal
===================
1. Check if the current node is empty / null.
2. Traverse the left subtree by recursively calling the in-order function.
3. Display the data part of the root (or current node).
4. Traverse the right subtree by recursively calling the in-order function.

Left -> Root -> Right

               4
           /      \
         2         6
        /  \     /   \
       1    3    5   7

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def in_order_print(self, start, traversal):
        if start:

            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.value) + ' -> ')
            traversal = self.in_order_print(start.right, traversal)

        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.in_order_print(tree.root, ""))
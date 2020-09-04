"""
ITERATIVE In-order Traversal
===================
1. Create list "stack" and variable "current" initially equal to root
2. While "stack" or "current:
    if "current":
        - append current to "stack"
        - move to the most left position from root
    else:
        - pop from "stack"
        - assigned popped to "current"

Left -> Root -> Right

               4
           /      \
         2         6
        /  \     /   \
       1    3    5   7

Given:
               1
           /      \
         2         3
        /  \     /   \
       4    5    6   7
Result = [4, 2, 5, 1, 6, 3, 7]

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def in_order_print(self):
        current = self.root
        node_stack = []
        result = []

        while current or node_stack:

            if current:
                node_stack.append(current)
                current = current.left

            else:
                current = node_stack.pop()
                result.append(current.value)
                current = current.right

        return result


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.in_order_print())
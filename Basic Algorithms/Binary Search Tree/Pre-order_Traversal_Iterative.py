"""
ITERATIVE Pre-order Traversal
===================
Use Stack

1. Create lists "stack" and "result"
2. Add root to "stack"
3. Pop it, record to "result"
4. If popped has right, add it to "stack"
5. If popped has left,  add it to "stack"
6. Repeat while stack > 0
7. Return result

Root -> Left -> Right
               1
           /      \
         2         5
        /  \     /   \
       3    4    6   7

Given:
               1
           /      \
         2         3
        /  \     /   \
       4    5    6   7
Result = [1, 2, 4, 5, 3, 6, 7]
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def pre_order_print(self):
        node_stack = [self.root]
        result = []

        while node_stack:
            current = node_stack.pop()
            result.append(current.value)

            if current.right:
                node_stack.append(current.right)

            if current.left:
                node_stack.append(current.left)

        return result


tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.pre_order_print())
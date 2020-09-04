"""
Post-order Traversal
===================
1. Check if the current node is empty / null.
2. Traverse the left subtree by recursively calling the post-order function.
3. Traverse the right subtree by recursively calling the post-order function.
4. Display the data part of the root (or current node).


Left -> Right -> Root

               7
           /      \
         3         6
        /  \     /   \
       1    2    4   5

Given:
               1
           /      \
         2         3
        /  \     /   \
       4    5    6   7

Result = [4, 5, 2, 6 ,7, 3, 1]
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def post_order_print(self):
        node_stack = [self.root]
        result = []

        while node_stack:
            current = node_stack.pop()
            result.append(current.value)

            if current.left:
                node_stack.append(current.left)

            if current.right:
                node_stack.append(current.right)

        return result[::-1]


tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.post_order_print())
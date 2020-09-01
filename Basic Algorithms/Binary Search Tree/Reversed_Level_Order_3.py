"""
        1
    /       \
  2           3
/   \       /   \
4   5       6   7

output: [6,7, 4,5, 2,3, 1]

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if not self.left:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if not self.right:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def reversed_level_trav(self):
        if not self.root:
            return

        queue = [self.root]
        stack = []
        traversal = ""

        while len(queue) > 0:
            node = queue.pop(0)
            if node.left or node.right:
                stack.insert(0, node)

            if node.right:
                queue.insert(0, node.right)

            if node.left:
                queue.insert(0, node.left)

        while len(stack) > 0:
            stack_node = stack.pop(0)
            if stack_node.left:
                traversal += str(stack_node.left.value) + ' - '
            if stack_node.right:
                traversal += str(stack_node.right.value) + ' - '
            if stack_node is self.root:
                traversal += str(stack_node.value)

        return traversal


tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)

array = [2, 3, 4, 5, 6, 7]
for element in array:
    tree.root.insert(element)

print(tree.reversed_level_trav())

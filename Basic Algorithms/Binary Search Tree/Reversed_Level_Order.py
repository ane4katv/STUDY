class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
            node = queue.pop()

            stack.append(node)

            if node.right:
                queue.append(node.right)

            if node.left:
                queue.append(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"




        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.reversed_level_trav())
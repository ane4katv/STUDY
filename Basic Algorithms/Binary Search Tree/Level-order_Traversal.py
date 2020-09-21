class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def level_order_trav(self):
        if not self.root:
            return

        queue = [self.root]
        traversal = []

        while len(queue) > 0:
            node = queue.pop(0)
            traversal.append(node.value)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.level_order_trav())
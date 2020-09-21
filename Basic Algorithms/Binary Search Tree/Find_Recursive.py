class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)

    def find(self, value):
        if self.root:
            is_found = self._find(value, self.root)
            if is_found:
                return True
            return False
        return None

    def _find(self, value, node):
        if value > node.value and node.right:
            return self._find(value, node.right)

        if value < node.value and node.left:
            return self._find(value, node.left)

        if value == node.value:
            return True

tree = BinarySearchTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.find(4))

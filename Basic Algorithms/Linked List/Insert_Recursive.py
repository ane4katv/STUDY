class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)

    def find(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node

        else:
            self._insert(value, self.root)


    def _insert(self, value, node):

        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._insert(value, node.left)

        elif value > node.value:
            if not node.right:
                node.right = Node(value)
            else:
                 self._insert(value, node.right)

        else:
            print("value is already present in the tree")

    def in_order(self, start, traversal):
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal += str(start.value)
            traversal = self.in_order(start.right, traversal)

        return traversal

tree = BinarySearchTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(8)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.in_order(tree.root, ""))

print(tree.insert(4))

print(tree.in_order(tree.root, ""))

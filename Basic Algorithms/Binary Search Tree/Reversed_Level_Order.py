"""
        1
    /       \
  2           3
/   \       /   \
4   5       6   7

output: [4,5,6,7,2,3,1]

"""
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

        while len(queue) > 0:
            queue = [self.root]
            traversal = []

            while len(queue) > 0:
                node = queue.pop(0)
                traversal.insert(0, node.value)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

            return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.reversed_level_trav())
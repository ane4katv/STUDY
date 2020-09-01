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

    def level_order_trav(self):
        if not self.root:
            return

        queue = [self.root]
        traversal = ""

        while len(queue) > 0:
            traversal += str(queue[0].value) + " - "
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return traversal[0:-2]

tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)

a = [2,3,4,5,6,7]
for i in a:
    tree.root.insert(i)

print(tree.level_order_trav())

print(tree.root.left)


"""
        1
    /       \
  2           3
/   \       /   \
4   5       6   7

output: [7,6,5,4,3,2,1]

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

        while len(queue) > 0:
            node = queue.pop()

            stack.insert(0,node)

            if node.left:
                queue.insert(0, node.left)

            if node.right:
                queue.insert(0, node.right)



        return [i.value for i in stack]


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
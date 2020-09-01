"""
Level-order Traversal (BF, Breadth First)
===================
Using Queue Data Structure

1. Peek and enqueue the root
2. De-queue the root
3. Check Left and Right children of de-queued root
4. Enqueue Left and then Right children
5. De-queue one by one
6. Repeat checking children and enqueueing/de-queueing each node

level 1 -> level 2 -> level 3    (all nodes on each level left to right)

               1        level 1
           /      \
         2         3    level 2
        /  \     /   \
       4    5    6   7  level 3

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def level_order_trav(self):
        traversal = ""
        queue = [self.root]

        while len(queue) != 0:

            traversal += str(queue[0].value) + ' - '

            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)

            queue.remove(queue[0])

        return traversal




tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.level_order_trav())
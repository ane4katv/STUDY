"""
        5
    /       \
  3           7
/   \       /   \
2   4       6   8

output: [6,8, 2,4, 3,7, 5]

"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def lst_to_levelorder_lst(self, array):
        left_part = sorted([array[i] for i in range(len(array)) if array[i] < self.root.value])
        right_part = sorted([array[i] for i in range(len(array)) if array[i] > self.root.value])

        self.root.left = self.lst_to_bst(left_part)
        self.root.right = self.lst_to_bst(right_part)

        if not self.root:
            return

        queue = [self.root]
        traversal = []

        while len(queue) > 0:
            traversal.append(queue[0].value)
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return traversal

    def lst_to_bst(self, array):
        if not array:
            return None

        mid = len(array) // 2

        node = Node(array[mid])

        node.left = self.lst_to_bst(array[:mid])
        node.right = self.lst_to_bst(array[mid + 1:])

        return node

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


tree = BinaryTree(5)
a = [2, 3, 4, 6, 7, 8]

print(tree.lst_to_levelorder_lst(a))
print(tree.reversed_level_trav())

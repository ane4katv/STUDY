# STACK
# LIFO
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = None

    def is_empty(self):
        if not self.head:
            return True
        return False

    def push(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if not self.is_empty():
            self.head = self.head.next
        else:
            return None


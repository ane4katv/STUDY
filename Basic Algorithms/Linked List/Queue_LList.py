# QUEUE
# FIFO

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)

class EmptyQueueException(Exception):
    pass

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data): # add to the end
        new_node = Node(data)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self.count += 1

    def dequeue(self):  # delete from beginning
        if self:
            self.head = self.head.next
            self.count -= 1
        else:
            raise EmptyQueueException

    def peek_front(self):
        if self:
            return self.head.data
        raise EmptyQueueException

    def peek_back(self):
        if self:
            return self.tail.data
        raise EmptyQueueException

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __bool__(self): # same as is_empty?
        return not (self.head is None and self.tail is None)

    def __contains__(self, data):
        return data in (node.data for node in self)

    def __len__(self):
        return self.count

    def __repr__(self):
        return ' -> '.join(str(node) for node in self)

llist = Queue()
llist.enqueue(5)
llist.enqueue(5)
llist.enqueue(5)
print(llist)











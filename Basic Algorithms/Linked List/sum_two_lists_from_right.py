class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node


    def is_empty(self):
        if not self.head:
            return True
        else:
            return False

    def pop(self):
        if not self.head:
            return None

        cur = self.head
        prev = None
        while cur.next:
            prev = cur
            cur = cur.next

        if cur == self.head:
            self.head = None

        popped = cur.data
        cur = None # doesn't seem it's being used

        if prev:
            prev.next = None

        return popped

    def sum_from_right(self,llist):

        sum_llist = LinkedList()

        carry = 0
        s = 0

        while not self.is_empty() and not llist.is_empty():
            s = (self.pop() + llist.pop() + carry)
            if s >= 10:
                carry = 1
                s -= 10
            else:
                carry = 0
            sum_llist.prepend(s)

        if not self.is_empty():
            while not self.is_empty():
                s = self.pop() + carry
                if s >= 10:
                    carry = 1
                    s -= 10
                else:
                    carry = 0
            sum_llist.prepend(s)

        if not llist.is_empty():
            while not llist.is_empty():
                s = llist.pop() + carry
                if s >= 10:
                    carry = 1
                    s -= 10
                else:
                    carry = 0
            sum_llist.prepend(s)

        sum_llist.print_list()


llist = LinkedList()
second_llist = LinkedList()

llist.prepend(3)
llist.prepend(2)
llist.prepend(1)

second_llist.prepend(7)
second_llist.prepend(8)


print("==== first list ====")
llist.print_list()

print("==== second list ====")
second_llist.print_list()

print("==== sum list ====")
llist.sum_from_right(second_llist)
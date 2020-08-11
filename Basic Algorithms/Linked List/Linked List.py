# https://realpython.com/linked-lists-python/#practical-applications

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))  # create a new node (head) by popping first element from nodes
            self.head = node  # first (popped) node becomes head
            for elem in nodes:
                node.next = Node(data=elem)  # create a new Node for each elem in nodes, make it "next"
                node = node.next  # created node.next becomes node and if there are more elems, loop continues

    def __repr__(self):  # represents list in printed form
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)  # add head.data to nodes list
            node = node.next  # node becomes next element to continue loop
        # nodes.append("None")  # when done append None to nodes list
        # return " -> ".join(nodes)
        return str(nodes)


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head  # point next to head
        self.head = node  # reassign head to node


    def add_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node


    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node, new_node):
        if not self.head:
            raise Exception("list is empty")
        if self.head.data == target_node:
            return self.add_first(new_node)

        prev = self.head
        for node in self:
            if node.data == target_node:
                prev.next = new_node
                new_node.next = node
                return
            prev = node
        raise Exception("No target number in the list")

    def remove_elem(self, target_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_data:
            self.head = self.head.next
            return

        prev = self.head
        for node in self:
            if node.data == target_data:
                prev.next = node.next
                return
            prev = node
        raise Exception("Target not found")




        # Create a method to retrieve an element from a specific position: get(i) or even llist[i].
    def retrieve_elem(self, index):
        count = 0
        for node in self:
            # print(count, index)
            if count == index:
                print(node.data)
                return
            count += 1

        raise Exception("index is not found")

    # Create a method to reverse the linked list: llist.reverse().
    def reverse(self):
        cur = self.head
        prev = None
        while cur is not None:
            next = cur.next

            cur.next = prev

            prev = cur
            cur = next

        self.head = prev

    # Create a Queue() object inheriting this article’s linked list with enqueue() and dequeue() methods.
    def enqueue(self, nodes):
        for node in nodes:
            self.add_last(node)

    def dequeue(self):
        for self.head in self:
            print(self.head.data)
            self.remove_node(self.head)




    # from “Cracking the Coding Interview” book.

    # 1. Traverse a linked list
    def traverse(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # 2. Remove duplicates from linked list
    def remove_dupes(self):

        prev = None
        cur = self.head
        uniques = []

        while cur is not None:
            if cur.data in uniques:
                prev.next = cur.next
            else:
                uniques.append(cur.data)

            prev = cur
            cur = cur.next

        return uniques

    # 3. Get the kth to last element from a linked list
    def kth_to_last(self, k):
        if not self.head:
            raise Exception("Empty List")

        was_k = False
        for node in self:
            if node.data == k:
                was_k = True
            if was_k:
                print(node.data)
        if not was_k:
            print("Value is not found")

    # 4. Delete a node from a linked list
    def del_node(self, node_data):
        if self.head.data == node_data:
            self.head = self.head.next
            return self

        prev = self.head
        for cur in self:
            if cur.data == node_data:
                prev.next = cur.next
            prev = cur

    # 5. Add two linked lists from left to right

    # 6. Add two linked lists from right to left


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

        if self.head is None:
            return None

        cur = self.head
        prev = None

        while cur.next:
            prev = cur
            cur = cur.next

        if cur == self.head:
            self.head = None

        popped = cur.data

        if prev:
            prev.next = None

        return popped

    def sum_from_right(self, llist):

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

        print(sum_llist)



llist = LinkedList([1, 2, 3])

llist2 = LinkedList([8, 7])

llist.sum_from_right(llist2)

llist.pop()

# llist.enqueue([Node(2), Node(3)])





# 8. Write a Python program to create a doubly linked list,
# append some items and iterate through the list (print forward).

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def iterate(self):
        cur = self.head
        while cur:
            # cur_data = cur.data
            yield cur
            cur = cur.next

    def print_forward(self):
        print([node.data for node in self.iterate()])

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    # 9. Write a Python program to print nodes from current position to first node.

    def print_backward_from_target(self, target):
        cur = self.tail
        while cur.prev:
            if cur.data == target:
                pass
            cur = cur.prev
            print(cur.data)


# dllist = Doubly_Linked_List()
#
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)
#
# dllist.print_back_from_target(3)


    # 10. Write a Python program to count the number of items of a given doubly linked list
    def count_items(self):
        print(self.count)

        # If append (with its count += 1) wasn't used)
        # cur = self.head
        # if not cur:
        #     return 0
        # for i in self.iterate():
        #     pass
        # print(self.count)

# llist = Doubly_Linked_List()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.count_items()
#
# print("I could do this too! Look, it is the same: ", llist.count)




    # 11. Write a Python program to print a given doubly linked list in reverse order

    def print_reverse_doubly_llist(self):
        cur = self.tail

        if not cur:
            return

        while cur:
            print(cur.data)
            cur = cur.prev


    def reverse_doubly_llist(self):
        cur = self.head
        while cur:
            next_temp = cur.next  # save it to keep moving forward and assign prev
            cur.next = cur.prev
            cur.prev = next_temp

            cur = next_temp

        self.head, self.tail = self.tail, self.head

# llist = Doubly_Linked_List()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
#
# llist.print_reverse_doubly_llist()
# llist.reverse_doubly_llist()
#
# print("************************")
# llist.print_forward()


    # 12. Write a Python program to insert an item in front of a given doubly linked list.
    def front_insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

        self.count += 1

# llist = Doubly_Linked_List()
# llist.append(777)
# llist.front_insert(2)
# llist.front_insert(3)
# llist.front_insert(4)
#
# llist.print_forward()

    # 13. Write a Python program to search a specific item in a given doubly linked list
    # and return true if the item is found otherwise return false.

    def search_elem(self, data):

        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

        # ALTERNATIVE:
        #
        # for node in self.iterate():
        #     if node.data == data:
        #         return True
        # return False

# llist = Doubly_Linked_List()
# llist.append(777)
# llist.front_insert(2)
# llist.front_insert(3)
# llist.front_insert(4)
#
# print(llist.search_elem(777))
# print(llist.search_elem(2))
# print(llist.search_elem(3))
# print(llist.search_elem(4))
# print(llist.search_elem(555))

    # 14. Write a Python program to delete a specific item from a given doubly linked list
    def del_elem(self, data):
        node_deleted = False
        cur = self.head

        if self.head is None:
            node_deleted = False

        elif self.head.data == data:
            self.head = cur.next

            node_deleted = True

        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None

            node_deleted = True

        else:
            while cur:
                if cur.data == data:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev

                    node_deleted = True

                cur = cur.next

        if node_deleted:
             self.count -= 1


llist = Doubly_Linked_List()
llist.append(1)
llist.front_insert(2)
llist.front_insert(3)
llist.front_insert(4)

llist.print_forward()

# print(llist.del_elem(4))
# llist.del_elem(2)
# llist.del_elem(3)
# llist.del_elem(4)
llist.del_elem(4)

llist.print_forward()


















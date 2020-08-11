class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


# 1. Write a Python program to create a singly linked list,
    # append some items and iterate through the list.

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node


    def iterate(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

# llist = LinkedList()
#
# a = [1,2,3,4,5]
#
# for i in a:
#     llist.append(i)
#
# for i in llist.iterate():
#     print(i.data)

# 2. Write a Python program to find the size of a singly linked list.


    def count_size(self):
        count = 0
        if not self.head:
            return count
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

# llist = LinkedList()
#
# a = [1,2,3,4,5]
#
# for i in a:
#     llist.append(i)
#
# print(llist.count_size())

# 3. Write a Python program to search a specific item
# in a singly linked list and return true if the item is found otherwise return false.

    def node_finder(self, node):
        if node:
            return True
        else:
            return False

    def elem_finder(self, data):
        for elem in self.iterate():
            if elem.data == data:
                return True
        return False

# llist = LinkedList()
#
# a = [1, 2, 3]
#
# for i in a:
#     llist.append(i)
#
# print(llist.node_finder(llist.head.next))
# print(llist.node_finder(llist.head.next.next.next))
# print(llist.elem_finder(3))
# print(llist.elem_finder(5))

# 4. Write a Python program to access a specific item
# in a singly linked list using index value.

    def elem_finder_by_index(self, index):
        count = 0

        cur = self.head
        while cur:
            if count == index:
                return cur.data
            count += 1
            cur = cur.next
        return "Index is not found"

# llist = LinkedList()
#
# a = [1, 2, 3]
#
# for i in a:
#     llist.append(i)
#
# print(llist.elem_finder_by_index(0))
# print(llist.elem_finder_by_index(1))
# print(llist.elem_finder_by_index(2))
# print(llist.elem_finder_by_index(3))

# 5. Write a Python program to set a new value
# of an item in a singly linked list using index value.

    def set_new_val(self, index, data):
        count = 0
        cur = self.head

        while cur:
            if count == index:
                cur.data = data
                return cur.data
            cur = cur.next
            count += 1
        return "Element with given index is not found"

# llist = LinkedList()
#
# a = [1, 2, 3]
#
# for i in a:
#     llist.append(i)
#
# print(llist.set_new_val(0, 999))
# print(llist.set_new_val(1, 999))
# print(llist.set_new_val(2, 999))
# print(llist.set_new_val(3, 999))

# 6. Write a Python program to delete the first item from a singly linked list.

    def delete_first(self):
        if not self.head:
            print("List is empty")

        elif not self.head.next:
            self.head = None

        else:
            self.head = self.head.next
#
# llist = LinkedList()
# a = [1,2,3,4,5]
# for i in a:
#     llist.append(i)
#
# llist.delete_first()
# print([i.data for i in llist.iterate()])

# 7. Write a Python program to delete the last item from a singly linked list.

    def delete_last(self):
        cur = self.head
        prev = None

        if not cur:
            print("List is empty")
            return

        if not cur.next:
            self.head = None
            return

        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None # or cur.next

# llist = LinkedList()
# a = [1,2,3,5]
# for i in a:
#     llist.append(i)
#
# llist.delete_last()
# print([i.data for i in llist.iterate()])

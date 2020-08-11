class DoublyLL:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


a = DoublyLL(1)
b = DoublyLL(2)
c = DoublyLL(3)

a.next = b
b.prev = a
b.next = c
c.prev = b

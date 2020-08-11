# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance


class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, price, author, pages):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price, publisher, period)


class Newspaper(Periodical):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price, publisher, period)


b1 = Book("Brave New World", 29.0, "Aldous Huxley", 311)
n1 = Newspaper("NY Times", 6.0, "New York Times Company", "Daily")
m1 = Magazine("Scientific American", 5.99, "Springer Nature", "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
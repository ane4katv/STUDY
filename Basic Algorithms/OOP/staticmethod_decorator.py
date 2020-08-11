class Book:

    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")


    #double underscore properties are hidden from other classes
    __booklist = None

    # static method
    @staticmethod
    def get_booklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist


    def set_title(self, new_title):
        self.new_title = new_title

    def __init__(self, title, book_type):
        self.title = title
        if book_type not in Book.BOOK_TYPES:
            raise ValueError(f"{book_type} is not a valid book type")
        else:
            self.book_type = book_type


b1 = Book("First Title", "PAPERBACK")
b2 = Book("Second Title", "EBOOK")


# Use static method to access a singleton object
the_books = Book.get_booklist()

the_books.append(b1)
the_books.append(b2)
print(the_books)


'''A singleton is a class that allows only a single instance of itself 
to be created and gives access to that created instance. 
It contains static variables that can accommodate unique 
and private instances of itself. It is used in scenarios 
when a user wants to restrict instantiation of a class to only one object'''

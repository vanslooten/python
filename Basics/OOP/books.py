# Example of classes and objects in Python, representing books in a library

class Book: # blueprint of objects of type Book
    def __init__(self, title):
        self.title = title

    def getTitle(self):
        return self.title

class Library:
    def __init__(self):
        self.books = [] # empty list

    def addBook(self, book): # add book object to list
        self.books.append(book)

    def showTitles(self):
        # Display titles of all books
        for i in range(len(self.books)):
            b = self.books[i]
            print(b.getTitle())

# Example usage:
if __name__ == "__main__":
    library = Library()
    library.addBook(Book("1984"))
    library.addBook(Book("Brave New World"))
    library.showTitles()

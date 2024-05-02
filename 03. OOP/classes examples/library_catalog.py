class LibraryCatalog:
    """
    A class representing a library catalog with functionalities to add, remove, and search for books.
    """

    def __init__(self):
        """
        Initializes a LibraryCatalog instance with an empty list of books.
        """
        self.books = []
        
    def add_book(self, title, author, isbn, copies):
        """
        Adds a book to the catalog or increments the number of copies if the book already exists.
        """
        for book in self.books:
            if book['isbn'] == isbn:
                book['copies'] += 1
                return
        self.books.append({'title': title, 'author': author, 'isbn': isbn, 'copies': copies})
            
    def remove_book(self,isbn):
        """
        Removes a book from the catalog or decreases the number of copies if available.
        """
        for book in self.books:
            if book['isbn'] == isbn:
                if book['copies'] >= 1:
                    book['copies'] -= 1
                    return
                else:
                    raise ValueError(f"No copies of book with ISBN: {isbn} available")    
        raise ValueError(f"Book with ISBN {isbn} not found in the catalog")
        
    def search_by_author(self, author):
        """
        Searches for books in the catalog by the specified author.
        """
        matching_books = []
        for book in self.books:
            if book['author'] == author:
                matching_books.append(book)
        return matching_books
  
    def search_by_title(self, title):
        """
        Searches for books in the catalog by the specified title.
        """
        matching_titles = []
        for book in self.books:
            if book['title'] == title:
                matching_titles.append(book)
        return matching_titles
    
    def get_catalog(self):
        """
        Retrieves the entire catalog of books.
        """
        return self.books
    
# Create a new library catalog
library = LibraryCatalog()

# Add books to the catalog
library.add_book("Harry Potter and the philosophers's Stone", "J.K. Rowling", "97898", 5)
library.add_book("The Hobbit", "J.R.R. Tolkien", "97803", 3)
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "97807", 2)
print(library.get_catalog())

print("Books by J.K. Rowling:")
for book in library.search_by_author("J.K. Rowling"):
    print(book)

# Remove a book from the catalog
library.remove_book("97803")

print("Updated Library Catalog:")
for book in library.get_catalog():
    print(book)

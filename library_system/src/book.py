"""
Book class representing a book in the library
"""

class Book:
    """Represents a book with title, author, year, genre, and ISBN."""
    
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        """
        Initialize a Book object.
        
        Args:
            title: The title of the book
            author: The author of the book
            year: The publication year
            genre: The genre of the book
            isbn: The ISBN of the book
        """
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    
    def __repr__(self):
        """Return a string representation of the book."""
        return f"Book(title='{self.title}', author='{self.author}', year={self.year}, genre='{self.genre}', isbn='{self.isbn}')"
    
    def __eq__(self, other):
        """Check equality between two books based on ISBN."""
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn
    
    def __hash__(self):
        """Make the book hashable based on ISBN."""
        return hash(self.isbn)
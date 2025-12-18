"""
List-based collection for books
"""

from typing import List, Union, Optional
from .book import Book


class BookCollection:
    """A list-based collection for storing books with list-like operations."""
    
    def __init__(self, books: Optional[List[Book]] = None):
        """
        Initialize the book collection.
        
        Args:
            books: Initial list of books (optional)
        """
        self._books = books or []
    
    def __getitem__(self, key: Union[int, slice]) -> Union[Book, 'BookCollection']:
        """
        Get item(s) by index or slice.
        
        Args:
            key: Index or slice
            
        Returns:
            A single book if key is an integer, or a new BookCollection if key is a slice
        """
        if isinstance(key, slice):
            return BookCollection(books=self._books[key])
        return self._books[key]
    
    def __iter__(self):
        """Iterate over the books in the collection."""
        return iter(self._books)
    
    def __len__(self) -> int:
        """Get the number of books in the collection."""
        return len(self._books)
    
    def __repr__(self) -> str:
        """String representation of the collection."""
        return f"BookCollection(books={self._books})"
    
    def append(self, book: Book) -> None:
        """Add a book to the collection."""
        self._books.append(book)
    
    def remove(self, book: Book) -> None:
        """Remove a book from the collection."""
        self._books.remove(book)
    
    def extend(self, books: List[Book]) -> None:
        """Extend the collection with multiple books."""
        self._books.extend(books)
    
    def clear(self) -> None:
        """Clear all books from the collection."""
        self._books.clear()
    
    def index(self, book: Book) -> int:
        """Find the index of a book in the collection."""
        return self._books.index(book)
    
    def count(self, book: Book) -> int:
        """Count occurrences of a book in the collection."""
        return self._books.count(book)
    
    def get_books_by_author(self, author: str) -> 'BookCollection':
        """Get all books by a specific author."""
        matching_books = [book for book in self._books if book.author == author]
        return BookCollection(books=matching_books)
    
    def get_books_by_year(self, year: int) -> 'BookCollection':
        """Get all books published in a specific year."""
        matching_books = [book for book in self._books if book.year == year]
        return BookCollection(books=matching_books)
    
    def get_books_by_genre(self, genre: str) -> 'BookCollection':
        """Get all books of a specific genre."""
        matching_books = [book for book in self._books if book.genre == genre]
        return BookCollection(books=matching_books)
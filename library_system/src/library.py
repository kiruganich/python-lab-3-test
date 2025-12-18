"""
Library class implementing the main library management system
"""

import logging
from typing import List, Optional
from .library_base import LibraryItem
from .book import Book
from .book_collection import BookCollection
from .index_dict import IndexDict


class Library(LibraryItem):
    """Main library class that manages books and their indices."""
    
    def __init__(self, name: str = "Main Library"):
        """
        Initialize the library.
        
        Args:
            name: Name of the library
        """
        super().__init__(name)
        self.books = BookCollection()
        self.indices = IndexDict()
        self.logger.info(f"Library '{self.name}' initialized with {len(self.books)} books")
    
    def add_book(self, book: Book) -> bool:
        """
        Add a book to the library.
        
        Args:
            book: The book to add
            
        Returns:
            True if the book was added, False if it already existed
        """
        if book in self.books:
            self.logger.warning(f"Book already exists: {book.title}")
            return False
        
        self.books.append(book)
        self.indices.add_book(book)
        self.logger.info(f"Added book: {book.title} by {book.author}")
        return True
    
    def remove_book(self, book: Book) -> bool:
        """
        Remove a book from the library.
        
        Args:
            book: The book to remove
            
        Returns:
            True if the book was removed, False if it didn't exist
        """
        try:
            self.books.remove(book)
            self.indices.remove_book(book)
            self.logger.info(f"Removed book: {book.title} by {book.author}")
            return True
        except ValueError:
            self.logger.warning(f"Book not found: {book.title}")
            return False
    
    def search_by_title(self, title: str) -> List[Book]:
        """
        Search for books by title.
        
        Args:
            title: Title to search for
            
        Returns:
            List of books with matching title
        """
        matching_books = [book for book in self.books if title.lower() in book.title.lower()]
        self.logger.info(f"Searched for books with title containing '{title}', found {len(matching_books)} results")
        return matching_books
    
    def search_by_author(self, author: str) -> List[Book]:
        """
        Search for books by author.
        
        Args:
            author: Author to search for
            
        Returns:
            List of books by the author
        """
        # Use the index for efficient search
        matching_books = self.indices.get_by_author(author)
        self.logger.info(f"Searched for books by author '{author}', found {len(matching_books)} results")
        return matching_books
    
    def search_by_genre(self, genre: str) -> List[Book]:
        """
        Search for books by genre.
        
        Args:
            genre: Genre to search for
            
        Returns:
            List of books of the genre
        """
        matching_books = [book for book in self.books if book.genre.lower() == genre.lower()]
        self.logger.info(f"Searched for books in genre '{genre}', found {len(matching_books)} results")
        return matching_books
    
    def search_by_year(self, year: int) -> List[Book]:
        """
        Search for books by year.
        
        Args:
            year: Year to search for
            
        Returns:
            List of books published in the year
        """
        # Use the index for efficient search
        matching_books = self.indices.get_by_year(year)
        self.logger.info(f"Searched for books published in {year}, found {len(matching_books)} results")
        return matching_books
    
    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        """
        Search for a book by ISBN.
        
        Args:
            isbn: ISBN to search for
            
        Returns:
            Book with the given ISBN or None if not found
        """
        book = self.indices.get_by_isbn(isbn)
        if book:
            self.logger.info(f"Found book by ISBN '{isbn}': {book.title}")
        else:
            self.logger.info(f"No book found with ISBN '{isbn}'")
        return book
    
    def display_info(self) -> str:
        """Display information about the library."""
        return f"Library '{self.name}' contains {len(self.books)} books"
    
    def __call__(self, query: str, search_type: str = "title") -> List[Book]:
        """
        Make the library callable for searching.
        
        Args:
            query: Query string to search for
            search_type: Type of search ('title', 'author', 'genre', 'year')
            
        Returns:
            List of matching books
        """
        self.logger.info(f"Searching for '{query}' by {search_type}")
        if search_type == "title":
            return self.search_by_title(query)
        elif search_type == "author":
            return self.search_by_author(query)
        elif search_type == "genre":
            return self.search_by_genre(query)
        elif search_type == "year":
            try:
                year = int(query)
                return self.search_by_year(year)
            except ValueError:
                self.logger.error(f"Invalid year: {query}")
                return []
        else:
            self.logger.error(f"Unknown search type: {search_type}")
            return []
    
    def get_total_books(self) -> int:
        """Get the total number of books in the library."""
        return len(self.books)
    
    def get_unique_authors(self) -> int:
        """Get the number of unique authors in the library."""
        authors = set(book.author for book in self.books)
        return len(authors)
    
    def get_books_by_year_range(self, start_year: int, end_year: int) -> List[Book]:
        """
        Get books published within a year range.
        
        Args:
            start_year: Start year of the range
            end_year: End year of the range
            
        Returns:
            List of books published within the range
        """
        matching_books = [
            book for book in self.books 
            if start_year <= book.year <= end_year
        ]
        self.logger.info(f"Found {len(matching_books)} books published between {start_year} and {end_year}")
        return matching_books
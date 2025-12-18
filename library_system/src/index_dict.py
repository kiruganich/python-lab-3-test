"""
Dictionary-based collection for indexing books by ISBN, author, and year
"""

import logging
from typing import Dict, List, Any, Union
from .book import Book


class IndexDict:
    """A dictionary-based collection for indexing books by ISBN, author, and year."""
    
    def __init__(self):
        """Initialize the index dictionary with empty indices."""
        self._indices = {
            'isbn': {},      # ISBN -> Book
            'author': {},    # Author -> List of Books
            'year': {}       # Year -> List of Books
        }
        self.logger = logging.getLogger(__name__)
    
    def __getitem__(self, key: Union[str, tuple]) -> Any:
        """
        Get indexed items by key.
        
        Args:
            key: Either a string (for ISBN lookup) or a tuple (index_type, value)
            
        Returns:
            A book (for ISBN) or list of books (for author/year)
        """
        if isinstance(key, tuple) and len(key) == 2:
            index_type, value = key
            if index_type in self._indices:
                return self._indices[index_type].get(value, [])
        elif isinstance(key, str):
            # Assume it's an ISBN lookup
            return self._indices['isbn'].get(key)
        raise KeyError(f"Invalid key: {key}")
    
    def __setitem__(self, key: Union[str, tuple], value: Union[Book, List[Book]]) -> None:
        """
        Set indexed items by key (this method is used internally).
        
        Args:
            key: Either a string (for ISBN) or a tuple (index_type, value)
            value: A book or list of books
        """
        if isinstance(key, tuple) and len(key) == 2:
            index_type, index_key = key
            if index_type in self._indices:
                self._indices[index_type][index_key] = value
                self.logger.info(f"Updated {index_type} index for '{index_key}'")
        elif isinstance(key, str):
            # Assume it's an ISBN
            self._indices['isbn'][key] = value
            self.logger.info(f"Added ISBN index for '{key}'")
    
    def __iter__(self):
        """Iterate over all indexed keys."""
        # Return all keys from all indices
        all_keys = set()
        for index_type, index_map in self._indices.items():
            for idx_key in index_map.keys():
                all_keys.add((index_type, idx_key))
        return iter(all_keys)
    
    def __len__(self) -> int:
        """Get total number of indexed entries across all indices."""
        total = 0
        for index_map in self._indices.values():
            total += len(index_map)
        return total
    
    def add_book(self, book: Book) -> None:
        """
        Add a book to all indices.
        
        Args:
            book: The book to add to indices
        """
        # Add to ISBN index
        self._indices['isbn'][book.isbn] = book
        
        # Add to author index
        if book.author not in self._indices['author']:
            self._indices['author'][book.author] = []
        self._indices['author'][book.author].append(book)
        
        # Add to year index
        if book.year not in self._indices['year']:
            self._indices['year'][book.year] = []
        self._indices['year'][book.year].append(book)
        
        self.logger.info(f"Indexed book: {book.title} by {book.author} ({book.year})")
    
    def remove_book(self, book: Book) -> None:
        """
        Remove a book from all indices.
        
        Args:
            book: The book to remove from indices
        """
        # Remove from ISBN index
        if book.isbn in self._indices['isbn']:
            del self._indices['isbn'][book.isbn]
        
        # Remove from author index
        if book.author in self._indices['author']:
            self._indices['author'][book.author] = [
                b for b in self._indices['author'][book.author] if b != book
            ]
            if not self._indices['author'][book.author]:  # If list is empty, remove key
                del self._indices['author'][book.author]
        
        # Remove from year index
        if book.year in self._indices['year']:
            self._indices['year'][book.year] = [
                b for b in self._indices['year'][book.year] if b != book
            ]
            if not self._indices['year'][book.year]:  # If list is empty, remove key
                del self._indices['year'][book.year]
        
        self.logger.info(f"Removed book from index: {book.title} by {book.author} ({book.year})")
    
    def get_by_isbn(self, isbn: str) -> Book:
        """
        Get a book by ISBN.
        
        Args:
            isbn: The ISBN to look up
            
        Returns:
            The book with the given ISBN
        """
        return self._indices['isbn'].get(isbn)
    
    def get_by_author(self, author: str) -> List[Book]:
        """
        Get all books by an author.
        
        Args:
            author: The author to look up
            
        Returns:
            List of books by the author
        """
        return self._indices['author'].get(author, [])
    
    def get_by_year(self, year: int) -> List[Book]:
        """
        Get all books published in a year.
        
        Args:
            year: The year to look up
            
        Returns:
            List of books published in the year
        """
        return self._indices['year'].get(year, [])
    
    def get_all_indices(self) -> Dict[str, Dict]:
        """
        Get all indices.
        
        Returns:
            Dictionary containing all indices
        """
        return self._indices.copy()
    
    def update_index(self) -> None:
        """Update the index (placeholder for future functionality)."""
        self.logger.info("Index updated")
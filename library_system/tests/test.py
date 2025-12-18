"""
Tests for the Library Management System
"""

import pytest
from src.book import Book
from src.book_collection import BookCollection
from src.index_dict import IndexDict
from src.library import Library
from src.simulation import generate_random_book, run_simulation


class TestBook:
    """Test cases for the Book class."""
    
    def test_book_creation(self):
        """Test creating a book."""
        book = Book("Title", "Author", 2023, "Fiction", "1234567890")
        assert book.title == "Title"
        assert book.author == "Author"
        assert book.year == 2023
        assert book.genre == "Fiction"
        assert book.isbn == "1234567890"
    
    def test_book_repr(self):
        """Test string representation of a book."""
        book = Book("Title", "Author", 2023, "Fiction", "1234567890")
        expected = "Book(title='Title', author='Author', year=2023, genre='Fiction', isbn='1234567890')"
        assert repr(book) == expected
    
    def test_book_equality(self):
        """Test equality comparison between books."""
        book1 = Book("Title", "Author", 2023, "Fiction", "1234567890")
        book2 = Book("Title", "Author", 2023, "Fiction", "1234567890")
        book3 = Book("Different", "Author", 2023, "Fiction", "0987654321")
        
        assert book1 == book2
        assert book1 != book3
        assert book1 != "not a book"


class TestBookCollection:
    """Test cases for the BookCollection class."""
    
    def test_book_collection_creation(self):
        """Test creating an empty book collection."""
        collection = BookCollection()
        assert len(collection) == 0
    
    def test_book_collection_with_initial_books(self):
        """Test creating a book collection with initial books."""
        book1 = Book("Title1", "Author1", 2023, "Fiction", "1234567890")
        book2 = Book("Title2", "Author2", 2022, "Non-Fiction", "0987654321")
        collection = BookCollection([book1, book2])
        assert len(collection) == 2
        assert collection[0] == book1
        assert collection[1] == book2
    
    def test_book_collection_append_and_len(self):
        """Test appending books and getting length."""
        collection = BookCollection()
        book = Book("Title", "Author", 2023, "Fiction", "1234567890")
        collection.append(book)
        assert len(collection) == 1
        assert collection[0] == book
    
    def test_book_collection_getitem_by_index(self):
        """Test getting a book by index."""
        book1 = Book("Title1", "Author1", 2023, "Fiction", "1234567890")
        book2 = Book("Title2", "Author2", 2022, "Non-Fiction", "0987654321")
        collection = BookCollection([book1, book2])
        
        assert collection[0] == book1
        assert collection[1] == book2
    
    def test_book_collection_getitem_by_slice(self):
        """Test getting books by slice."""
        book1 = Book("Title1", "Author1", 2023, "Fiction", "1234567890")
        book2 = Book("Title2", "Author2", 2022, "Non-Fiction", "0987654321")
        book3 = Book("Title3", "Author3", 2021, "Mystery", "1111111111")
        collection = BookCollection([book1, book2, book3])
        
        sliced_collection = collection[0:2]
        assert len(sliced_collection) == 2
        assert sliced_collection[0] == book1
        assert sliced_collection[1] == book2
    
    def test_book_collection_iteration(self):
        """Test iterating over books in the collection."""
        book1 = Book("Title1", "Author1", 2023, "Fiction", "1234567890")
        book2 = Book("Title2", "Author2", 2022, "Non-Fiction", "0987654321")
        collection = BookCollection([book1, book2])
        
        books = list(collection)
        assert len(books) == 2
        assert books[0] == book1
        assert books[1] == book2
    
    def test_book_collection_remove(self):
        """Test removing a book from the collection."""
        book1 = Book("Title1", "Author1", 2023, "Fiction", "1234567890")
        book2 = Book("Title2", "Author2", 2022, "Non-Fiction", "0987654321")
        collection = BookCollection([book1, book2])
        
        collection.remove(book1)
        assert len(collection) == 1
        assert collection[0] == book2
    
    def test_book_collection_search_methods(self):
        """Test search methods in the collection."""
        book1 = Book("Title1", "Author1", 2023, "Fiction", "1234567890")
        book2 = Book("Title2", "Author1", 2022, "Non-Fiction", "0987654321")
        book3 = Book("Title3", "Author2", 2023, "Fiction", "1111111111")
        collection = BookCollection([book1, book2, book3])
        
        # Test by author
        author_books = collection.get_books_by_author("Author1")
        assert len(author_books) == 2
        assert book1 in author_books
        assert book2 in author_books
        
        # Test by year
        year_books = collection.get_books_by_year(2023)
        assert len(year_books) == 2
        assert book1 in year_books
        assert book3 in year_books
        
        # Test by genre
        genre_books = collection.get_books_by_genre("Fiction")
        assert len(genre_books) == 2
        assert book1 in genre_books
        assert book3 in genre_books


class TestIndexDict:
    """Test cases for the IndexDict class."""
    
    def test_index_dict_creation(self):
        """Test creating an empty index dictionary."""
        index_dict = IndexDict()
        assert len(index_dict) == 0
    
    def test_add_and_get_book_by_isbn(self):
        """Test adding and retrieving a book by ISBN."""
        index_dict = IndexDict()
        book = Book("Title", "Author", 2023, "Fiction", "1234567890")
        index_dict.add_book(book)
        
        retrieved_book = index_dict.get_by_isbn("1234567890")
        assert retrieved_book == book
    
    def test_add_and_get_books_by_author(self):
        """Test adding and retrieving books by author."""
        index_dict = IndexDict()
        book1 = Book("Title1", "Author1", 2023, "Fiction", "1234567890")
        book2 = Book("Title2", "Author1", 2022, "Non-Fiction", "0987654321")
        index_dict.add_book(book1)
        index_dict.add_book(book2)
        
        author_books = index_dict.get_by_author("Author1")
        assert len(author_books) == 2
        assert book1 in author_books
        assert book2 in author_books
    
    def test_add_and_get_books_by_year(self):
        """Test adding and retrieving books by year."""
        index_dict = IndexDict()
        book1 = Book("Title1", "Author1", 2023, "Fiction", "1234567890")
        book2 = Book("Title2", "Author2", 2023, "Non-Fiction", "0987654321")
        index_dict.add_book(book1)
        index_dict.add_book(book2)
        
        year_books = index_dict.get_by_year(2023)
        assert len(year_books) == 2
        assert book1 in year_books
        assert book2 in year_books
    
    def test_remove_book_from_indices(self):
        """Test removing a book from all indices."""
        index_dict = IndexDict()
        book = Book("Title", "Author", 2023, "Fiction", "1234567890")
        index_dict.add_book(book)
        
        # Verify book is in indices
        assert index_dict.get_by_isbn("1234567890") == book
        assert book in index_dict.get_by_author("Author")
        assert book in index_dict.get_by_year(2023)
        
        # Remove the book
        index_dict.remove_book(book)
        
        # Verify book is removed from all indices
        assert index_dict.get_by_isbn("1234567890") is None
        assert book not in index_dict.get_by_author("Author")
        assert book not in index_dict.get_by_year(2023)
    
    def test_index_dict_magic_methods(self):
        """Test magic methods of IndexDict."""
        index_dict = IndexDict()
        book = Book("Title", "Author", 2023, "Fiction", "1234567890")
        index_dict.add_book(book)
        
        # Test __len__
        assert len(index_dict) == 3  # 1 ISBN + 1 author + 1 year
        
        # Test __getitem__ with tuple
        author_books = index_dict[('author', 'Author')]
        assert len(author_books) == 1
        assert author_books[0] == book


class TestLibrary:
    """Test cases for the Library class."""
    
    def test_library_creation(self):
        """Test creating a library."""
        library = Library("Test Library")
        assert library.name == "Test Library"
        assert len(library.books) == 0
        assert library.display_info() == "Library 'Test Library' contains 0 books"
    
    def test_add_book(self):
        """Test adding a book to the library."""
        library = Library()
        book = Book("Title", "Author", 2023, "Fiction", "1234567890")
        
        result = library.add_book(book)
        assert result is True
        assert len(library.books) == 1
        assert library.books[0] == book
        assert library.search_by_isbn("1234567890") == book
    
    def test_remove_book(self):
        """Test removing a book from the library."""
        library = Library()
        book = Book("Title", "Author", 2023, "Fiction", "1234567890")
        library.add_book(book)
        
        result = library.remove_book(book)
        assert result is True
        assert len(library.books) == 0
        assert library.search_by_isbn("1234567890") is None
    
    def test_search_by_author(self):
        """Test searching for books by author."""
        library = Library()
        book1 = Book("Title1", "Author1", 2023, "Fiction", "1234567890")
        book2 = Book("Title2", "Author1", 2022, "Non-Fiction", "0987654321")
        library.add_book(book1)
        library.add_book(book2)
        
        results = library.search_by_author("Author1")
        assert len(results) == 2
        assert book1 in results
        assert book2 in results
    
    def test_search_by_year(self):
        """Test searching for books by year."""
        library = Library()
        book1 = Book("Title1", "Author1", 2023, "Fiction", "1234567890")
        book2 = Book("Title2", "Author2", 2023, "Non-Fiction", "0987654321")
        library.add_book(book1)
        library.add_book(book2)
        
        results = library.search_by_year(2023)
        assert len(results) == 2
        assert book1 in results
        assert book2 in results
    
    def test_call_method(self):
        """Test calling the library as a function."""
        library = Library()
        book = Book("Test Title", "Test Author", 2023, "Fiction", "1234567890")
        library.add_book(book)
        
        results = library("Test Author", "author")
        assert len(results) == 1
        assert results[0] == book


class TestSimulation:
    """Test cases for the simulation."""
    
    def test_generate_random_book(self):
        """Test generating a random book."""
        book = generate_random_book()
        assert isinstance(book, Book)
        assert book.title != ""
        assert book.author != ""
        assert 1900 <= book.year <= 2025
        assert book.genre != ""
        assert book.isbn != ""
    
    def test_run_simulation(self):
        """Test running the simulation."""
        # Just make sure it runs without errors
        run_simulation(steps=5, seed=42)
        assert True  # If we reach here, the simulation ran without errors
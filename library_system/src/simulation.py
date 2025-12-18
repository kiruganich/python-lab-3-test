"""
Simulation module for the library management system
"""

import random
import logging
from typing import List
from .constants import EVENT_TYPES, DEFAULT_STEPS, GENRES
from .library import Library
from .book import Book


def generate_random_book() -> Book:
    """Generate a random book for simulation purposes."""
    titles = [
        "The Great Adventure", "Mystery of the Old House", "Journey to the Unknown",
        "Secrets of the Forest", "Tales from the Past", "Dreams and Reality",
        "Echoes of Time", "Shadows and Light", "Legends of Tomorrow", "Whispers in the Wind"
    ]
    authors = [
        "John Smith", "Emily Johnson", "Michael Brown", "Sarah Davis", "Robert Wilson",
        "Jennifer Taylor", "David Anderson", "Lisa Martinez", "James Thomas", "Patricia Garcia"
    ]
    
    title = random.choice(titles)
    author = random.choice(authors)
    year = random.randint(1900, 2025)
    genre = random.choice(GENRES)
    isbn = f"{random.randint(1000000000, 9999999999)}"
    
    return Book(title=title, author=author, year=year, genre=genre, isbn=isbn)


def run_simulation(steps: int = DEFAULT_STEPS, seed: int | None = None) -> None:
    """
    Run the library simulation for a specified number of steps.
    
    Args:
        steps: Number of simulation steps to run
        seed: Random seed for reproducible results
    """
    if seed is not None:
        random.seed(seed)
        logging.info(f"Set random seed to {seed}")
    
    # Create a library instance
    library = Library(name="Simulation Library")
    logging.info(f"Starting simulation with {steps} steps")
    
    for step in range(steps):
        event_type = random.choice(EVENT_TYPES)
        logging.info(f"Step {step + 1}: Executing event '{event_type}'")
        
        if event_type == "add_book":
            book = generate_random_book()
            success = library.add_book(book)
            if success:
                print(f"Added book: {book.title} by {book.author}")
            else:
                print(f"Failed to add book (already exists): {book.title}")
                
        elif event_type == "remove_book":
            if len(library.books) > 0:
                # Pick a random book to remove
                book_idx = random.randint(0, len(library.books) - 1)
                book_to_remove = library.books[book_idx]
                success = library.remove_book(book_to_remove)
                if success:
                    print(f"Removed book: {book_to_remove.title} by {book_to_remove.author}")
                else:
                    print(f"Failed to remove book: {book_to_remove.title}")
            else:
                print("No books to remove")
                
        elif event_type == "search_author":
            if len(library.books) > 0:
                # Pick a random author from existing books
                sample_book = random.choice(list(library.books)) if hasattr(library.books, '__iter__') else library.books[0] if len(library.books) > 0 else None
                if sample_book:
                    results = library.search_by_author(sample_book.author)
                    print(f"Searched for author '{sample_book.author}', found {len(results)} books")
                else:
                    print("No books available for author search")
            else:
                print("No books in library for author search")
                
        elif event_type == "search_genre":
            if len(library.books) > 0:
                # Pick a random genre from existing books
                sample_book = random.choice(list(library.books)) if hasattr(library.books, '__iter__') else library.books[0] if len(library.books) > 0 else None
                if sample_book:
                    results = library.search_by_genre(sample_book.genre)
                    print(f"Searched for genre '{sample_book.genre}', found {len(results)} books")
                else:
                    print("No books available for genre search")
            else:
                print("No books in library for genre search")
                
        elif event_type == "search_year":
            if len(library.books) > 0:
                # Pick a random year from existing books
                sample_book = random.choice(list(library.books)) if hasattr(library.books, '__iter__') else library.books[0] if len(library.books) > 0 else None
                if sample_book:
                    results = library.search_by_year(sample_book.year)
                    print(f"Searched for year {sample_book.year}, found {len(results)} books")
                else:
                    print("No books available for year search")
            else:
                print("No books in library for year search")
                
        elif event_type == "update_index":
            library.indices.update_index()
            print("Updated library indices")
            
        elif event_type == "get_missing_book":
            # Try to get a book that doesn't exist
            fake_isbn = "9999999999999"
            book = library.search_by_isbn(fake_isbn)
            if book is None:
                print(f"Tried to get book with ISBN {fake_isbn}, book not found (as expected)")
            else:
                print(f"Unexpectedly found book with fake ISBN {fake_isbn}")
    
    # Print final library status
    print(f"\nSimulation completed!")
    print(f"Final library status: {library.display_info()}")
    print(f"Total unique authors: {library.get_unique_authors()}")
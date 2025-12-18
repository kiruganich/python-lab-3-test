"""
Constants for the Library Management System
"""

# Event types for simulation
EVENT_TYPES = [
    "add_book",
    "remove_book",
    "search_author",
    "search_genre",
    "search_year",
    "update_index",
    "get_missing_book"
]

# Default simulation parameters
DEFAULT_STEPS = 20
DEFAULT_SEED = 42

# Log format
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Supported genres
GENRES = [
    "Fiction", "Non-Fiction", "Mystery", "Romance", "Sci-Fi",
    "Fantasy", "Biography", "History", "Self-Help", "Poetry"
]
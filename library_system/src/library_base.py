"""
Base class for the Library system
"""

import logging
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Abstract base class for library items."""
    
    def __init__(self, name: str):
        """
        Initialize a library item.
        
        Args:
            name: Name of the library item
        """
        self.name = name
        self.logger = logging.getLogger(__name__)
    
    @abstractmethod
    def display_info(self) -> str:
        """Display information about the library item."""
        pass
    
    def __repr__(self) -> str:
        """String representation of the library item."""
        return f"{self.__class__.__name__}(name='{self.name}')"
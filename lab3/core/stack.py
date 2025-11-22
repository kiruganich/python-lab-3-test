"""
Module implementing Stack and MinStack data structures.
"""

class Stack:
    """
    Stack implementation using Python list.
    """
    
    def __init__(self):
        self._data = []
    
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        
        Args:
            x: Integer to push onto stack
        """
        self._data.append(x)
    
    def pop(self) -> int:
        """
        Remove and return the element from the top of the stack.
        
        Returns:
            The top element of the stack
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()
    
    def peek(self) -> int:
        """
        Return the element at the top of the stack without removing it.
        
        Returns:
            The top element of the stack
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            True if stack is empty, False otherwise
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Return the number of elements in the stack.
        
        Returns:
            Number of elements in the stack
        """
        return len(self._data)


class MinStack(Stack):
    """
    Stack that supports retrieving the minimum element in O(1) time.
    """
    
    def __init__(self):
        super().__init__()
        self._min_stack = []  # Auxiliary stack to keep track of minimums
    
    def push(self, x: int) -> None:
        """
        Push element x onto stack and update minimum.
        
        Args:
            x: Integer to push onto stack
        """
        super().push(x)
        
        # If min_stack is empty or x is smaller than or equal to current minimum, push to min_stack
        if not self._min_stack or x <= self._min_stack[-1]:
            self._min_stack.append(x)
    
    def pop(self) -> int:
        """
        Remove and return the element from the top of the stack.
        Update minimum accordingly.
        
        Returns:
            The top element of the stack
            
        Raises:
            IndexError: If stack is empty
        """
        value = super().pop()
        
        # If the popped value is the current minimum, remove it from min_stack
        if self._min_stack and value == self._min_stack[-1]:
            self._min_stack.pop()
        
        return value
    
    def min(self) -> int:
        """
        Return the minimum element in the stack in O(1) time.
        
        Returns:
            The minimum element in the stack
            
        Raises:
            IndexError: If stack is empty
        """
        if not self._min_stack:
            raise IndexError("min from empty stack")
        return self._min_stack[-1]
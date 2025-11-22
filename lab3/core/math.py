"""
Module implementing factorial and Fibonacci functions.
Both iterative and recursive versions are provided.
"""

def factorial(n: int) -> int:
    """
    Calculate factorial of n using iterative approach.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n < 0
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of n using recursive approach.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n < 0
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibo(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using iterative approach.
    fibo(0) = 0, fibo(1) = 1
    
    Args:
        n: Non-negative integer
        
    Returns:
        n-th Fibonacci number
        
    Raises:
        ValueError: If n < 0
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibo_recursive(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using recursive approach.
    fibo(0) = 0, fibo(1) = 1
    
    Args:
        n: Non-negative integer
        
    Returns:
        n-th Fibonacci number
        
    Raises:
        ValueError: If n < 0
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
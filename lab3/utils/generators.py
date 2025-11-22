"""
Module for generating various types of test arrays.
"""
import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Generate a random array of n integers in range [lo, hi].
    
    Args:
        n: Size of the array
        lo: Lower bound (inclusive)
        hi: Upper bound (inclusive)
        distinct: If True, all elements will be unique
        seed: Random seed for reproducibility
        
    Returns:
        Random array of integers
    """
    if seed is not None:
        random.seed(seed)
    
    if distinct:
        if hi - lo + 1 < n:
            raise ValueError(f"Not enough distinct integers in range [{lo}, {hi}] to fill array of size {n}")
        result = random.sample(range(lo, hi + 1), n)
    else:
        result = [random.randint(lo, hi) for _ in range(n)]
    
    return result


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Generate an array that is nearly sorted by starting with a sorted array
    and performing a specified number of random swaps.
    
    Args:
        n: Size of the array
        swaps: Number of swaps to perform
        seed: Random seed for reproducibility
        
    Returns:
        Nearly sorted array
    """
    if seed is not None:
        random.seed(seed)
    
    arr = list(range(n))  # Create sorted array [0, 1, ..., n-1]
    
    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Generate an array with many duplicate values.
    
    Args:
        n: Size of the array
        k_unique: Number of unique values to use
        seed: Random seed for reproducibility
        
    Returns:
        Array with many duplicates
    """
    if seed is not None:
        random.seed(seed)
    
    unique_values = list(range(k_unique))
    result = [random.choice(unique_values) for _ in range(n)]
    
    return result


def reverse_sorted(n: int) -> list[int]:
    """
    Generate an array sorted in reverse order.
    
    Args:
        n: Size of the array
        
    Returns:
        Reverse sorted array [n-1, n-2, ..., 1, 0]
    """
    return list(range(n-1, -1, -1))


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Generate a random array of n floats in range [lo, hi].
    
    Args:
        n: Size of the array
        lo: Lower bound
        hi: Upper bound
        seed: Random seed for reproducibility
        
    Returns:
        Random array of floats
    """
    if seed is not None:
        random.seed(seed)
    
    result = [random.uniform(lo, hi) for _ in range(n)]
    
    return result
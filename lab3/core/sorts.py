"""
Module implementing various sorting algorithms:
- Bubble sort
- Counting sort  
- Bucket sort
"""

def bubble_sort(a: list[int]) -> list[int]:
    """
    Sorts an array using bubble sort algorithm.
    
    Args:
        a: List of integers to sort
        
    Returns:
        New sorted list (does not modify original)
    """
    arr = a[:]  # Create a copy
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


def counting_sort(a: list[int]) -> list[int]:
    """
    Sorts an array using counting sort algorithm.
    Works with any integers (including negative).
    
    Args:
        a: List of integers to sort
        
    Returns:
        New sorted list (does not modify original)
    """
    if not a:
        return []
    
    # Find min and max values
    min_val = min(a)
    max_val = max(a)
    
    # Create count array
    range_size = max_val - min_val + 1
    count = [0] * range_size
    
    # Count occurrences of each element
    for num in a:
        count[num - min_val] += 1
    
    # Reconstruct the sorted array
    result = []
    for i in range(range_size):
        result.extend([i + min_val] * count[i])
    
    return result


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Sorts an array using bucket sort algorithm for floats.
    If elements are not in [0,1), normalizes them to this range first,
    then denormalizes back after sorting.
    
    Args:
        a: List of floats to sort
        buckets: Number of buckets to use (default: length of array)
        
    Returns:
        New sorted list (does not modify original)
    """
    if not a:
        return []
    
    if buckets is None:
        buckets = len(a)
    
    if buckets <= 0:
        return []
    
    # Determine if normalization is needed
    min_val = min(a)
    max_val = max(a)
    
    # If all elements are the same, return copy
    if min_val == max_val:
        return a[:]
    
    # Normalize values to [0, 1) range if needed
    normalized = []
    needs_normalization = min_val < 0 or max_val >= 1
    
    if needs_normalization:
        range_val = max_val - min_val
        if range_val == 0:
            return a[:]
        for val in a:
            normalized.append((val - min_val) / range_val)
    else:
        normalized = a[:]
    
    # Create buckets
    bucket_list = [[] for _ in range(buckets)]
    
    # Distribute elements into buckets
    for val in normalized:
        bucket_idx = min(int(val * buckets), buckets - 1)  # Clamp to prevent index out of range
        bucket_list[bucket_idx].append(val)
    
    # Sort individual buckets using bubble sort and concatenate
    result = []
    for bucket in bucket_list:
        # Use bubble sort to sort each bucket
        sorted_bucket = bubble_sort_int_list(bucket)
        result.extend(sorted_bucket)
    
    # Denormalize back to original range if normalization was applied
    if needs_normalization:
        range_val = max_val - min_val
        result = [val * range_val + min_val for val in result]
    
    return result


def bubble_sort_int_list(a: list[float]) -> list[float]:
    """
    Helper function to sort a list of floats using bubble sort.
    """
    arr = a[:]  # Create a copy
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
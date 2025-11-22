"""
Module for benchmarking algorithms.
"""
import time
from typing import Dict, Callable, Any


def timeit_once(func, *args, **kwargs) -> float:
    """
    Measure the execution time of a function in seconds.
    
    Args:
        func: Function to benchmark
        *args: Positional arguments for the function
        **kwargs: Keyword arguments for the function
        
    Returns:
        Execution time in seconds
    """
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    
    return end_time - start_time


def benchmark_sorts(arrays: Dict[str, list], algos: Dict[str, Callable]) -> Dict[str, Dict[str, float]]:
    """
    Benchmark sorting algorithms on different arrays.
    
    Args:
        arrays: Dictionary mapping array names to arrays
        algos: Dictionary mapping algorithm names to sorting functions
        
    Returns:
        Nested dictionary with timing results: {array_name: {algo_name: time_in_seconds}}
    """
    results = {}
    
    for array_name, array in arrays.items():
        results[array_name] = {}
        for algo_name, algo_func in algos.items():
            # Make a copy of the array to ensure fair comparison
            array_copy = array[:] if hasattr(array, '__getitem__') else array
            time_taken = timeit_once(algo_func, array_copy)
            results[array_name][algo_name] = time_taken
    
    return results
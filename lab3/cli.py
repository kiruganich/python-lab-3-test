#!/usr/bin/env python3
"""
CLI script to run benchmarks on sorting algorithms.
"""
import sys
from core.sorts import bubble_sort, counting_sort, bucket_sort
from utils.generators import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array
from utils.benchmark import benchmark_sorts


def main():
    """
    Main function to run benchmarks and display results.
    """
    print("Lab 3 - Algorithmic Mini-Package")
    print("Benchmarking Sorting Algorithms")
    print("=" * 50)
    
    # Generate test arrays
    int_arrays = {
        "Random (int)": rand_int_array(1000, 0, 1000, seed=42),
        "Nearly Sorted": nearly_sorted(1000, 50, seed=42),
        "Many Duplicates": many_duplicates(1000, k_unique=10, seed=42),
        "Reverse Sorted": reverse_sorted(1000),
    }
    
    float_arrays = {
        "Random (float)": rand_float_array(1000, 0.0, 1.0, seed=42)
    }
    
    # Define algorithms to test for integers
    int_algos = {
        "Bubble Sort": bubble_sort,
        "Counting Sort": counting_sort,
        "Bucket Sort (as float)": lambda x: bucket_sort([float(i) for i in x])
    }
    
    # Define algorithms to test for floats
    float_algos = {
        "Bubble Sort": lambda x: bubble_sort([float(i) for i in x]),
        "Bucket Sort": bucket_sort,
    }
    
    # Run benchmarks
    print("Running benchmarks for integer arrays...")
    int_results = benchmark_sorts(int_arrays, int_algos)
    
    print("Running benchmarks for float arrays...")
    float_results = benchmark_sorts(float_arrays, float_algos)
    
    # Combine results
    results = {**int_results, **float_results}
    
    # Display results in a table format
    print("\nBenchmark Results (Time in seconds):")
    print("-" * 80)
    
    # Print header for all algorithms
    all_algo_names = set()
    for res in results.values():
        all_algo_names.update(res.keys())
    all_algo_names = sorted(list(all_algo_names))
    
    header = f"{'Array Type':<20} | "
    for algo_name in all_algo_names:
        header += f"{algo_name:<15} | "
    print(header)
    print("-" * len(header))
    
    # Print results for each array
    for array_name in sorted(results.keys()):
        row = f"{array_name:<20} | "
        for algo_name in all_algo_names:
            time_taken = results[array_name].get(algo_name, 0.0)
            row += f"{time_taken:<15.6f} | "
        print(row)
    
    print("\nNote: For float arrays, all algorithms were applied appropriately.")
    print("Bucket sort is most efficient for uniformly distributed float data.")
    print("Counting sort is efficient for integer data with limited range.")
    print("Bubble sort has O(n^2) complexity and is generally slower.")


if __name__ == "__main__":
    main()
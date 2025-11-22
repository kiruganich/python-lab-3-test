Lab 3 - Algorithmic Mini-Package
===============================

This project implements various algorithms including factorial/fibonacci functions,
sorting algorithms, stack data structure, and benchmarking utilities.

## How to Run

### Prerequisites
- Python 3.8 or higher

### Running the CLI
To run the benchmarking CLI that tests all sorting algorithms on different array types:

```bash
cd /workspace/lab3
python cli.py
```

This will:
- Generate various test arrays (random, nearly sorted, with duplicates, reverse sorted)
- Run all three sorting algorithms (bubble, counting, bucket) on these arrays
- Display a performance comparison table in the console
- Generate a report.txt file with the results

### Running Individual Components
You can also test individual components:

```bash
# Test factorial and fibonacci functions
python -c "from core.math import factorial, fibo; print(factorial(5)); print(fibo(10))"

# Test sorting algorithms
python -c "from core.sorts import bubble_sort; print(bubble_sort([5,2,8,1]))"

# Test stack implementation
python -c "from core.stack import Stack; s = Stack(); s.push(1); print(s.pop())"
```

### Project Structure
```
lab3/
├── core/
│   ├── math.py          # factorial and fibonacci functions
│   ├── sorts.py         # sorting algorithms
│   └── stack.py         # stack data structures
├── utils/
│   ├── generators.py    # array generation functions
│   └── benchmark.py     # benchmarking utilities
├── cli.py               # main CLI entry point
├── report.txt           # generated benchmark report
└── README.md            # this file
```
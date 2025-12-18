"""
Main entry point for the Library Management System
"""

import argparse
import logging
from src.constants import LOG_FORMAT
from src.simulation import run_simulation


def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


def main():
    """Main function to run the library management system."""
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Library Management System")
    parser.add_argument('--steps', type=int, default=20, help='Number of simulation steps (default: 20)')
    parser.add_argument('--seed', type=int, help='Random seed for reproducible results')
    
    args = parser.parse_args()
    
    print("Starting Library Management System Simulation...")
    print(f"Running simulation with {args.steps} steps")
    if args.seed is not None:
        print(f"Using seed: {args.seed}")
    print("-" * 50)
    
    run_simulation(steps=args.steps, seed=args.seed)


if __name__ == "__main__":
    main()
"""
Exercise: Decorators

Problem:
Write a decorator that measures and prints the execution time of a function in seconds.

Then use this decorator on a function that creates a list from 1 to n.

Input:
A number n indicating the size of the list.

Output:
The execution time in seconds
"""

import time
from typing import Callable


def timing(func: Callable[[int], list]) -> Callable[[int], list]:
    """
    Decorator to measure and print the execution time of a function in seconds.
    """
    def wrapper(n: int) -> list:
        start = time.time()
        result = func(n)
        end = time.time()
        duration = end - start
        print(f"Execution time: {duration:.5} seconds")
        return result
    return wrapper


@timing
def generate_numbers(n: int) -> list:
    """
    Generate a list from 1 to n (inclusive).
    """
    return [i for i in range(1, n + 1)]


def main() -> None:
    """
    Main function to get input and print the generated list and execution time.
    """
    try:
        size = int(input("Please enter the size of sequence: ").strip())
        generate_numbers(size)
    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()

"""
Exercise: Sum of Multiple Numbers

Problem:
Write a function named `sum_numbers(*args)` that takes any number of integers as input and
returns their sum.
- If no numbers are provided, the function should return 0.

Input:
- A list of integers provided as input.

Output:
- The sum of all the provided integers.
- If no numbers are provided, return 0.

Sample Input 1:
5 10 15

Sample Output 1:
30

Sample Input 2:
7 3 2 1 9

Sample Output 2:
22
"""


def sum_numbers(*args):
    """
    Returns the sum of all provided numbers.

    Parameters:
    - *args (int): Any number of integers.

    Returns:
    - int: The sum of all input integers. If no integers are provided, returns 0.
    """
    return sum(args)  # Efficiently using the built-in sum function


def main():
    """
    Reads a list of numbers from input and prints the sum of these numbers.
    """
    numbers = [int(i) for i in input(
        "Please enter numbers separated by spaces: ").split()]
    print(sum_numbers(*numbers))


if __name__ == "__main__":
    main()

"""
Exercise: Positive Number Check

Problem:
Write a function named `is_positive` that takes an integer as input
and returns `True` if the number is positive or zero, 
and `False` otherwise (if the number is negative).

Input:
- A single integer.

Output:
- `True` if the number is positive or zero.
- `False` if the number is negative.

Sample Input 1:
5

Sample Output 1:
True

Sample Input 2:
-3

Sample Output 2:
False
"""


def is_positive(n):
    """
    Checks if a number is positive or zero.

    Parameters:
    - n (int): The number to check.

    Returns:
    - bool: True if n is positive or zero, False if n is negative.
    """
    return n >= 0


def main():
    """
    Reads an integer from input and prints whether it is positive or zero.
    """
    num = int(input("Enter an integer: "))
    print(is_positive(num))


if __name__ == "__main__":
    main()

"""
Exercise: Check if a Number is Even or Odd

Problem:
Write a function named `is_even` that checks if the given number is even or odd.

The function should return:
- `True` if the number is even.
- `False` if the number is odd.

Input:
- An integer `n` which will be read from the input.

Output:
- `True` if `n` is even.
- `False` if `n` is odd.

Sample Input 1:
8

Sample Output 1:
True

Sample Input 2:
15

Sample Output 2:
False
"""


def is_even(n):
    """
    Checks if a number is even.

    Parameters:
    - n (int): The integer to check.

    Returns:
    - bool: True if n is even, False if n is odd.
    """
    return n % 2 == 0


def main():
    """
    Reads an integer from input and prints whether the number is even or odd.
    """
    num = int(input("Please enter a number: "))
    print(is_even(num))


if __name__ == "__main__":
    main()

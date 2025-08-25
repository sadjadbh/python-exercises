"""
Exercise: Check if One Number is Greater than Another

Problem:
Write a function named `is_greater` that checks if the first number is greater than the second.

The function should return:
- `True` if `a` is greater than `b`.
- `False` if `a` is less than or equal to `b`.

Input:
- Two integers `a` and `b`.

Output:
- `True` if `a > b`.
- `False` if `a <= b`.

Sample Input 1:
10
5

Sample Output 1:
True

Sample Input 2:
3
7

Sample Output 2:
False
"""


def is_greater(a, b):
    """
    Checks if the first number is greater than the second.

    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.

    Returns:
    - bool: True if a is greater than b, False otherwise.
    """
    return a > b


def main():
    """
    Reads two integers from input and prints whether the first is greater than the second.
    """
    n1 = int(input("Please enter the first number: "))
    n2 = int(input("Please enter the second number: "))
    print(is_greater(n1, n2))


if __name__ == "__main__":
    main()

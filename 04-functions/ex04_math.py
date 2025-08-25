"""
Exercise: Sum of Squares of Two Numbers

Problem:
Write a function named `sum_of_squares` that takes two integers as input and
returns the sum of their squares.

The formula to calculate the sum of squares is:
sum_of_squares(a, b) = a**2 + b**2

Input:
- Two integers `a` and `b`.

Output:
- A single integer representing the sum of the squares of `a` and `b`.

Sample Input 1:
3
4

Sample Output 1:
25

Sample Input 2:
5
12

Sample Output 2:
169
"""


def sum_of_squares(x1, x2):
    """
    Returns the sum of squares of two integers.

    Parameters:
    - x1 (int): The first integer.
    - x2 (int): The second integer.

    Returns:
    - int: The sum of the squares of x1 and x2.
    """
    return x1**2 + x2**2


def main():
    """
    Reads two integers from input and prints the sum of their squares.
    """
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    print(sum_of_squares(num1, num2))


if __name__ == "__main__":
    main()

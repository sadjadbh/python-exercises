"""
Exercise: Chained Comparison in Python

Problem:
Write a program that takes three integers a, b, and c as input.
Check whether the condition a < b <= c is True or not.
If it is, print True; otherwise, print False.

Sample Input:
5
10
15

Sample Output:
True
"""


def check_comparison(a, b, c):
    """Return True if a < b <= c, otherwise False."""
    return a < b <= c


def main():
    """
    Reads three integers and prints whether they satisfy `a < b <= c`.

    This function serves as the primary entry point of the script. It prompts
    the user to enter three integer values for a, b, and c, then checks
    if the chained comparison `a < b <= c` is true. The boolean result
    is printed to the console.
    """
    # Read three integers from the user
    a = int(input("Enter first number (a): "))
    b = int(input("Enter second number (b): "))
    c = int(input("Enter third number (c): "))

    # Check the condition and print the result
    result = check_comparison(a, b, c)
    print(result)


if __name__ == "__main__":
    main()

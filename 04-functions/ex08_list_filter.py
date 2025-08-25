"""
Exercise: Pick Even Numbers

Problem:
Write a function named `pick_evens(*args)` that receives multiple numbers as input and
returns a list containing only the even numbers.
- If no even numbers are provided, the function should return an empty list `[]`.

Input:
- A list of integers provided as input.

Output:
- A list containing only the even numbers from the input.
- If there are no even numbers, return an empty list `[]`.

Sample Input 1:
1 2 3 4 5 6

Sample Output 1:
[2, 4, 6]

Sample Input 2:
7 13 19 21

Sample Output 2:
[]
"""


def pick_evens(*args):
    """
    Filters and returns only the even numbers from the input.

    Parameters:
    - *args (int): Any number of integers.

    Returns:
    - list: A list containing only even numbers from the input.
            Returns an empty list if no even numbers are provided.
    """
    return [number for number in args if number % 2 == 0]


def main():
    """
    Reads a list of numbers from input and prints only the even numbers.
    """
    nums = [int(i) for i in input(
        "Please enter numbers separated by spaces: ").split()]
    print(pick_evens(*nums))


if __name__ == "__main__":
    main()

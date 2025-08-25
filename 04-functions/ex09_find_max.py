"""
Exercise: Find the Tallest Building (Skyline)

Problem:
Write a function named `skyline(*args)` that receives the heights of several buildings as input and
returns the height of the tallest building.
- If no heights are provided, return 0.

Input:
- A list of integers representing the heights of buildings.

Output:
- The height of the tallest building.
- If no heights are provided, return 0.

Sample Input 1:
3 7 15 2 9

Sample Output 1:
15

Sample Input 2:
1 1 1 1

Sample Output 2:
1
"""


def skyline(*args):
    """
    Returns the height of the tallest building from the input heights.

    Parameters:
    - *args (int): Heights of buildings.

    Returns:
    - int: The height of the tallest building, or 0 if no heights are provided.
    """
    return max(args, default=0)


def main():
    """
    Reads the heights of buildings from input and prints the height of the tallest building.
    """
    heights = [int(i) for i in input(
        "Please enter the heights of the buildings separated by spaces: ").split()]
    print(skyline(*heights))


if __name__ == "__main__":
    main()

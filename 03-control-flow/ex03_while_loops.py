"""
Exercise: Magic Machine Sequence to 1

Problem:
A magic machine takes an initial number `n` and repeatedly transforms it until it becomes 1.
The machine performs the following operations:

- If the current number is even, divide it by 2.
- If the current number is odd, multiply it by 3 and add 1.

The program should print the number at each step until it reaches 1.

Input:
- A single integer `n` (2 ≤ n ≤ 1000) representing the starting number.

Output:
- The sequence of numbers starting from `n` and ending at 1, each printed on a new line.

Sample Input:
50

Sample Output:
50
25
76
38
19
58
29
88
44
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
"""


def magic_machine(n):
    """Performs the transformation steps until n reaches 1."""
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(1)


def main():
    """
    Handles user input to start the magic machine sequence.

    This function serves as the script's entry point. It prompts the user
    for a starting integer, validates that it is within the accepted
    range of [2, 1000], and then calls the `magic_machine` function
    to run and print the sequence. If the input is invalid, it
    prints an error message instead.
    """
    # Gets input from user and runs the magic machine process.
    n = int(input("Enter an integer between 2 and 1000: "))
    if 2 <= n <= 1000:
        magic_machine(n)
    else:
        print("Invalid input. Please enter a number between 2 and 1000.")


if __name__ == "__main__":
    main()

"""
Exercise: Wizard's Power Enhancement Spell

Problem:
A wizard casts a spell to increase the power of numbers.
The wizard selects an initial number `x` and performs `n` operations on it. The operations are:

- If the number is odd, multiply it by 2 and subtract 1.
- If the number is even, divide it by 2.

The wizard performs these operations `n` times.

Input:
- An integer `n` representing the number of steps (1 ≤ n ≤ 20).
- An integer `x` representing the initial value (1 ≤ x ≤ 1000).

Output:
- The final value of `x` after performing the operations `n` times.

Sample Input:
5
10

Sample Output:
65
"""


def enhance_power(n, x):
    """Perform the wizard's power enhancement spell for n steps."""
    for _ in range(n):
        if x % 2 == 0:
            x /= 2
        else:
            x = (x * 2) - 1
    return int(x)


def main():
    """
    Gets user input and runs the wizard's power enhancement simulation.

    This function serves as the main driver for the script. It prompts the
    user to enter the number of spell steps (`n`) and an initial value (`x`).
    After validating that the inputs are within the allowed range, it calls the
    `enhance_power` function to perform the calculation and prints the final
    result to the console.
    """
    # Get the number of steps (n) and the initial value (x) from the user
    n = int(input("Enter the number of steps (1 ≤ n ≤ 20): "))
    x = int(input("Enter the initial value (1 ≤ x ≤ 1000): "))

    # Validate inputs (if needed, but in this case the problem guarantees valid input)
    if 1 <= x <= 1000 and 1 <= n <= 20:
        final_value = enhance_power(n, x)
        print(f"The final value after {n} steps is: {final_value}")
    else:
        print("Invalid input. Please enter values within the specified range.")


if __name__ == "__main__":
    main()

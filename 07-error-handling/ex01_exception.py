"""
Exercise: Error Handling; The Division Function

Problem:
The following function is intended to receive two numbers and return the result of their division.
However, the current code has some issues that need to be fixed.

Original Code:
    def divide(a, b):
        result = a / b
        return result

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Result:", divide(num1, num2))

Tasks:
1. If `num2 = 0`, a ZeroDivisionError occurs. Handle this error gracefully.
2. If the user inputs a non-numeric value (e.g., "hello"), a ValueError occurs. Handle it properly.
3. After the function runs, show a message "Program has run successfully!", even if an error occurred.
4. The program should not crash! It must ask the user again for correct inputs if invalid values are entered.
"""


def get_number(prompt: str) -> float:
    """
    Prompt the user to enter a number (integer or float).
    Repeats until valid input is received.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid value! Please enter a number.")


def divide(a: float, b: float) -> float | None:
    """
    Divide a by b. Handle division by zero.
    Return the result or None if division failed.
    Always print a message when the function finishes.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    finally:
        print("Program has run successfully!")


def main() -> None:
    """
    Main function to run the safe division program.
    """
    first = get_number("Please enter the first number: ")
    second = get_number("Please enter the second number: ")
    result = divide(first, second)

    if result is not None:
        print(f"Result: {result:.2f}")
    else:
        print("Could not compute the result due to an error.")


if __name__ == "__main__":
    main()

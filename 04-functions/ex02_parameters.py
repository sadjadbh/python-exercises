"""
Exercise: Personalized Greeting

Problem:
Write a function called `greet` that takes a name as input and prints "Hello, Name!", 
where `Name` is replaced by the provided input.

Input:
- A single string representing a person's name.

Output:
- The message "Hello, Name!" printed to the screen.

Sample Input:
Ali

Sample Output:
Hello, Ali!
"""


def greet(name):
    """
    Prints a greeting message that includes the provided name.

    Parameters:
    - name (str): The name to include in the greeting.
    """
    print(f"Hello, {name}!")


def main():
    """
    Reads a name from input and calls the greet function to display the greeting.
    """
    person = input("please enter your name: ")
    greet(person)


if __name__ == "__main__":
    main()

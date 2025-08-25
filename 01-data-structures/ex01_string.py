"""
Exercise: Convert and Split a String

Problem:
Write a program that takes the following string, converts it to lowercase,
and then returns it as a list of individual words using string methods.

String:
txt = 'Hi this is a string'

Expected Output:
['hi', 'this', 'is', 'a', 'string']
"""


def convert_and_split(text):
    """Lowercase converting and spliting a string"""
    return text.lower().split()


def main():
    """
    Create a sample string, apply `convert_and_split` to it,
    and print the modified result.
    """
    txt = "Hi this is a string"
    result = convert_and_split(txt)
    print(result)


if __name__ == "__main__":
    main()

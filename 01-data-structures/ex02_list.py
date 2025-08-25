"""
Exercise: Add and Remove List Items

Problem:
Given a list, remove the number 3 using list operations (not slicing or comprehensions),
append the number 10 to the end of the list, and returns the updated list.

Input:
my_list = [1, 2, 3, 4, 5]

Expected Output:
[1, 2, 4, 5, 10]
"""


def modify_list(lst):
    """Removing the number 3 and adding the number 10 to the list"""
    lst.remove(3)
    lst.append(10)
    return lst


def main():
    """
    Create a sample list, apply `modify_list` to it,
    and print the modified result.
    """
    my_list = [1, 2, 3, 4, 5]
    result = modify_list(my_list)
    print(result)


if __name__ == "__main__":
    main()

"""
Exercise: Union and Intersection of Sets

Problem:
You are given two magical sets, set_a and set_b, containing distinct numbers.  
Your task is to calculate and print the union and intersection of these two sets.

Example:
set_a = {1, 2, 3, 4}  
set_b = {3, 4, 5, 6}  

1. Find the union of set_a and set_b.  
2. Find the intersection of set_a and set_b.

Output:
Union: {1, 2, 3, 4, 5, 6}  
Intersection: {3, 4}
"""


def calculate_union(set_a, set_b):
    """Return the union of two sets."""
    return set_a.union(set_b)


def calculate_intersection(set_a, set_b):
    """Return the intersection of two sets."""
    return set_a.intersection(set_b)


def main():
    """
    Demonstrates set operations by defining two sets, calculating their 
    union and intersection, and printing the results.

    - set_a: {1, 2, 3, 4}
    - set_b: {3, 4, 5, 6}

    Uses the functions `calculate_union` and `calculate_intersection`.
    """
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    # Calculate union and intersection
    union_set = calculate_union(set_a, set_b)
    intersection_set = calculate_intersection(set_a, set_b)

    # Display results
    print(f"Union: {union_set}")
    print(f"Intersection: {intersection_set}")


if __name__ == "__main__":
    main()

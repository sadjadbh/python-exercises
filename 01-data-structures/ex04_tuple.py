"""
Exercise: Distance between two points using tuple

Problem:
Create a tuple named `coordinates` which includes coordinates of point A in the plane (a = (3, 4)).  
Then, write a code to calculate the distance between this point and the origin (0, 0).  
Use the Euclidean distance formula to calculate the distance between two points in the
coordinate plane.

Formula:
distance = √((x₂ - x₁)² + (y₂ - y₁)²)
"""

from math import sqrt


def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def main():
    """
    Creates two points (A and the origin), uses `calculate_distance` to
    compute the distance between them, and prints the result.
    """

    # Coordinates of point A (3, 4)
    coordinates = (3, 4)

    # Origin (0, 0)
    origin = (0, 0)

    # Calculate and print the Euclidean distance
    dist = calculate_distance(coordinates, origin)
    print(
        f"The distance between the point {coordinates} and the origin {origin} is {dist}")


if __name__ == "__main__":
    main()

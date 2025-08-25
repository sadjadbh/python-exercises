"""
Manages the creation and loading of a dice roll data file.

This module provides functions to generate a binary file (`dice_rolls.pkl`)
containing random dice roll data and a generator to load that data.
It can be run as a script to create the data file.
"""

import random
import pickle
import os

ROLLS_FILE = 'dice_rolls.pkl'


def generate_rolls(num_rolls=100):
    """
    Generates a specified number of dice roll pairs (tuples)
    and saves them to a binary file using pickle.
    """
    print(f"Generating {num_rolls} dice rolls...")
    # Use a list comprehension for a concise way to build the list
    rolls = [(random.randint(1, 6), random.randint(1, 6))
             for _ in range(num_rolls)]

    with open(ROLLS_FILE, 'wb') as file:
        pickle.dump(rolls, file)

    print(f"Successfully saved rolls to '{ROLLS_FILE}'.")


def load_rolls():
    """
    A generator function that loads dice rolls from the file and yields them
    one by one.
    """
    # Check if the data file exists before trying to open it
    if not os.path.exists(ROLLS_FILE):
        print(f"Error: Data file '{ROLLS_FILE}' not found.")
        print("Please run 'python dice_manager.py' first to generate it.")
        return

    with open(ROLLS_FILE, 'rb') as file:
        rolls_data = pickle.load(file)

    # 'yield from' is an elegant way to yield all items from another iterable
    yield from rolls_data


# This block runs only when the script is executed directly
if __name__ == '__main__':
    generate_rolls()

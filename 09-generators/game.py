"""
Runs a simple dice game by loading and displaying pre-generated rolls.

This script uses a generator from the `dice_manager` module and `itertools.islice`
to efficiently load and display a limited number of dice rolls from the data file.
"""

import itertools
from dice_manager import load_rolls

# Set the number of turns for the game
MAX_TURNS = 6

print("--- Welcome to the Dice Game! ---")
print(f"Showing the first {MAX_TURNS} pre-generated rolls.")

# load_rolls() returns a generator.
# We use itertools.islice to get the first MAX_TURNS items from the generator.
# This is memory-efficient as it doesn't process the whole file at once.
rolls_generator = load_rolls()
limited_rolls = itertools.islice(rolls_generator, MAX_TURNS)

# The enumerate function adds a turn counter automatically
for turn_number, roll in enumerate(limited_rolls, start=1):
    # If the generator is empty (e.g., file not found), this loop won't run.
    # The 'roll' is a tuple like (die1, die2)
    die1, die2 = roll
    print(
        f"Turn {turn_number}: You rolled a {die1} and a {die2}. Total: {die1 + die2}")

print("\n--- Game Over! ---")

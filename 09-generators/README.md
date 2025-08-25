# Dice Roll Game 🎲

A simple Python project that demonstrates data generation, file I/O with `pickle`, and the use of generators.

The project is split into two main parts:
1.  A script to generate and save a list of dice rolls.
2.  A game script that reads these rolls using a generator.

---

## File Structure

* `dice_manager.py`: A module to handle the data file. It can generate a new `dice_rolls.pkl` file containing 100 random dice rolls. It also provides a generator function to load these rolls.
* `game.py`: The main game script. It imports the loader from `dice_manager.py` and displays the first 6 dice rolls from the generated file.
* `dice_rolls.pkl`: The data file created by `dice_manager.py`. This is a binary file and should not be edited manually.

---

## How to Run the Game

You need to run the scripts from your terminal in two steps.

### Step 1: Generate the Dice Rolls

First, run the `dice_manager.py` script. This will create the `dice_rolls.pkl` file in the same directory.

```bash
python dice_manager.py
```
### Step 2: Play the Game

Once the data file is created, you can run the game.

```bash
python game.py
```
The game will load the rolls and display the first 6 results. The output will look something like this:

--- Welcome to the Dice Game! ---
Showing the first 6 pre-generated rolls.
Turn 1: You rolled a 4 and a 2. Total: 6
Turn 2: You rolled a 1 and a 6. Total: 7
Turn 3: You rolled a 3 and a 3. Total: 6
Turn 4: You rolled a 5 and a 1. Total: 6
Turn 5: You rolled a 2 and a 4. Total: 6
Turn 6: You rolled a 6 and a 5. Total: 11

--- Game Over! ---
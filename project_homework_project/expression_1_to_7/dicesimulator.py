"""
Program: Dice Simulator
-----------------------
This program simulates rolling two dice, three times.
For each roll, it prints the total of the two dice.
It is designed to demonstrate how variable scope works in Python.
Variables with the same name can exist in different scopes (e.g., inside `main()` vs. inside `roll_dice()`),
and they do not interfere with each other.
"""

import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    The variables die1 and die2 here are local to this function.
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    """
    Main function to simulate three dice rolls and demonstrate scope.
    The die1 variable here is local to main() and does not affect roll_dice().
    """
    die1: int = 10
    print("\ndie1 in main() starts as:", die1)
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() ends as:", die1)

# Call the main() function only when this file is executed directly.
if __name__ == '__main__':
    main()

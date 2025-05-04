"""
Program: Dice Simulator
------------------------
This program simulates rolling two dice, prints the results of each die roll,
and also prints the total of the two rolls.

It demonstrates:
- Using the random module to simulate the dice rolls.
- Generating random numbers within a range.
- Calculating the total of two dice rolls and printing the results.
"""

# Import the random library to simulate random dice rolls
import random

# Number of sides on each die
NUM_SIDES: int = 6

def main():
    # Roll the dice by generating random numbers between 1 and NUM_SIDES (inclusive)
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Calculate the total of the two dice rolls
    total: int = die1 + die2
    
    # Print the results
    print(f"\nDice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

# This line calls the main() function when the script is executed
if __name__ == '__main__':
    main()

# This program counts from 1 to 10 but might stop early depending on randomness.
# The `done()` function simulates a random "I'm done" decision with a set likelihood.

import random

DONE_LIKELIHOOD = 0.2  # Probability of stopping early (you can tweak this!)

def done():
    """Returns True with a probability of DONE_LIKELIHOOD."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):  # Loop from 1 to 10
        if done():
            return  # Stop early if done() returns True
        print("\n", i)

def main():
    print("\nI'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == "__main__":
    main()

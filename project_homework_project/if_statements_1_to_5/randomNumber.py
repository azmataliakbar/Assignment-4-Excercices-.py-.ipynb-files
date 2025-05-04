
# This program prints 10 random numbers in the range 1 to 100.
# Each time you run the program, it generates a different set of numbers
# using Python's built-in random number generator.

import random

N_NUMBERS: int = 10      # Total numbers to print
MIN_VALUE: int = 1       # Minimum value in range
MAX_VALUE: int = 100     # Maximum value in range

def main():
    for _ in range(N_NUMBERS):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print("\n",number, end=" ")  # Print all numbers on the same line with a space

# This line ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()

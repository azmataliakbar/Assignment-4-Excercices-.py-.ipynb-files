"""
Program: Pythagorean Theorem Calculator
---------------------------------------
This program calculates the length of the hypotenuse (BC) of a right triangle
when the lengths of the two perpendicular sides (AB and AC) are known.

It demonstrates:
- Taking float input from the user,
- Using the Pythagorean theorem: BC² = AB² + AC²,
- Using the math library for square root,
- Formatting the output to 2 decimal places.
"""

import math  # Needed for square root calculation

def main():
    # Prompt user to enter the two perpendicular sides
    ab: float = float(input("\nEnter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Compute hypotenuse using the Pythagorean theorem
    bc: float = math.sqrt(ab**2 + ac**2)

    # Output the result with two decimal places
    print(f"The length of BC (the hypotenuse) is: {bc:.2f}")

# Required to call main when script is run
if __name__ == '__main__':
    main()

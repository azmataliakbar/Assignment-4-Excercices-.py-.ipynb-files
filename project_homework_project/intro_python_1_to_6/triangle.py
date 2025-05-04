"""
Program: triangle_perimeter
---------------------------
This program prompts the user to input the lengths of the
three sides of a triangle and calculates the perimeter
by summing the side lengths.
"""

def main():
    PERIMETER_MSG = "The perimeter of the triangle is "
    print("\nperimeter = side1 + side2 + side3")
    # Get the 3 side lengths of the triangle
    side1: float = float(input("\nWhat is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    # Calculate and print the perimeter
    perimeter: float = side1 + side2 + side3
    print(PERIMETER_MSG + str(perimeter))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

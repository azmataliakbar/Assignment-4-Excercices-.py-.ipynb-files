"""
Program: square_calculator
--------------------------
This program prompts the user to enter a number and
displays the square of that number.
"""

def main():
    SQUARE_MSG = " squared is "

    # Get number from the user and calculate its square
    num: float = float(input("\nType a number to see its square: "))
    square: float = num ** 2

    # Print the result
    print(str(num) + SQUARE_MSG + str(square))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

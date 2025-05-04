# This program asks the user to enter a number,
# and then prints the ones digit (last digit) of that number using the modulo operator.

def print_ones_digit(num: int):
    """
    Prints the ones digit of the given number.
    """
    print("After division & calculation, the ones digit is", num % 10)

def main():
    num = int(input("\nEnter a number: "))
    print_ones_digit(num)

# Required to run the main function
if __name__ == '__main__':
    main()

# This program displays a list of numbers from 10 to 19
# and prints each number followed by whether it is even or odd.
# It uses a helper function `is_odd()` to determine the parity of each number.

def is_odd(value: int):
    """
    Checks if a value is odd. Returns True if it is, else False.
    """
    return value % 2 == 1

def main():
    numbers = list(range(10, 20))  # Create list from 10 to 19
    print("\nGiven integers:\n", numbers)  # Print the list

    for i in numbers:
        if is_odd(i):
            print(f"\n{i} odd", end=" ")
        else:
            print(f"\n{i} even", end=" ")

# Required to run the main function when the script is executed
if __name__ == '__main__':
    main()


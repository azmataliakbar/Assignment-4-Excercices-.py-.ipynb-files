# This program asks the user for a number and prints all the divisors of that number.
# A divisor is any number that divides the given number exactly (no remainder).
# The function print_divisors(num) is used to handle this logic.

def print_divisors(num: int):
    """
    Prints all the divisors of the input number.
    A divisor divides the number exactly (remainder is zero).
    """
    divisors = []  # Create a list to store divisors
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)  # Add valid divisor to the list

    print(f"\nHere are the divisors of {num}")
    print(divisors)  # Print the full list of divisors

def main():
    num = int(input("\nEnter a number: "))  # Ask user for input
    print_divisors(num)  # Call helper function

# Required to run the main function
if __name__ == '__main__':
    main()

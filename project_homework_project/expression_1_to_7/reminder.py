"""
Program: Division with Remainder
--------------------------------
This program divides two integers, one entered by the user to be divided (dividend),
and the other as the divisor. It prints the quotient (result of division) and the remainder.

It demonstrates:
- Integer division to find the quotient,
- Modulo operation to find the remainder,
- Reading and handling user input.
"""

def main():
    # Ask the user for the dividend and divisor
    dividend: int = int(input("\nPlease enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Perform division and find the remainder
    quotient: int = dividend // divisor  # Integer division (quotient)
    remainder: int = dividend % divisor  # Remainder (modulo operation)

    # Output the results
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# This line calls the main() function when the script is executed
if __name__ == '__main__':
    main()

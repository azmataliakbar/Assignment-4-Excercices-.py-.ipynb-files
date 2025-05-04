# This Python program defines a function called square() that returns the square of a number.
# It then uses a loop to call this function for the numbers 1 through 5 and prints each result.

def square(n):
    return n * n  # Return the square of the input number

def main():
    for i in range(1, 6):  # Loop from 1 to 5
        result = square(i)
        print(f"\nThe square of {i} is {result}")  # Display the result

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

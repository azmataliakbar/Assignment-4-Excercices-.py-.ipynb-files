# This Python program asks the user to enter a number, then repeatedly doubles that number,
# printing each result, until the value becomes 100 or greater.

def main():
    curr_value = int(input("Enter a number: "))  # Get the starting number from the user
    curr_value = curr_value * 2  # First doubling

    while curr_value < 100:
        print("\n", curr_value)
        curr_value = curr_value * 2  # Keep doubling the value

    print("\n", curr_value)  # Print the final value that is >= 100

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

# This program asks the user to enter values one by one.
# Each entered value is added to a list.
# When the user presses Enter without typing anything, the loop ends,
# and the complete list of values is printed.

def main():
    lst = []  # Create an empty list to store values

    val = input("\nEnter a value: ")  # Ask for the first value
    while val:  # Keep running as long as input is not empty
        lst.append(val)  # Add the value to the list
        val = input("\nEnter a value: ")  # Ask for the next value

    print("\nHere's the complete list of all elements: ", lst)  # Print the final list

# This provided line is required to call main() when the script runs
if __name__ == '__main__':
    main()

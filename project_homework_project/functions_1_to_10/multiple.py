# This program asks the user for a message and a number,
# then prints the message that number of times.
# The function print_multiple(message, repeats) handles the repetition logic.

def print_multiple(message: str, repeats: int):
    """
    Prints the given message the specified number of times.
    """
    messages = []  # Create a list to store repeated messages
    for _ in range(repeats):
        messages.append(message)
    print("\nHere is your repeated message:")
    print(messages)  # Print all messages as a list

def main():
    message = input("\nPlease type a message: ")  # Get message from user
    repeats = int(input("\nEnter a number of times to repeat your message: "))  # Get repeat count
    print_multiple(message, repeats)  # Call function

# Required to run the main function
if __name__ == '__main__':
    main()

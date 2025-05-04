"""
This program asks the user to enter their name and then greets them using a helper function.
The `greet(name)` function generates a greeting message.
The `main()` function handles user input and displays the greeting.
"""

def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.
    """
    return "Greetings " + name + "!"

def main():
    # Prompt user for their name
    name = input("\nWhat's your name? ")
    
    # Greet the user
    print("\n", greet(name))

# This line ensures main() runs when the file is executed
if __name__ == '__main__':
    main()

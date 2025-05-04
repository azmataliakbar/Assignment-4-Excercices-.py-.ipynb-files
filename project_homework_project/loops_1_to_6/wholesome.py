# This Python program prompts the user to type a specific affirmation.
# It keeps asking the user to type the exact affirmation until it is entered correctly.
# The goal is to help users internalize a positive message by repeating it exactly.

AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("\nPlease type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get user's input
    while user_feedback != AFFIRMATION:  # Keep looping until the input matches the affirmation
        print("\nThat was not the affirmation.")
        print("\nPlease type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("\nThat's right! :)")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

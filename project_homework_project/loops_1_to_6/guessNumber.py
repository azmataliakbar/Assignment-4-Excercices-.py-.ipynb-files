# This Python program implements a simple number guessing game.
# The computer randomly selects a number between 1 and 99, and the user tries to guess it.
# After each guess, the program tells the user whether the guess was too high or too low.
# When the correct number is guessed, the program congratulates the user and ends.

import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)
    
    print("\nI am thinking of a number between 1 and 99...")
    
    # Get user's first guess
    guess = int(input("\nEnter a guess: "))
    
    # Keep asking until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Empty line for better readability
        guess = int(input("\nEnter a new guess: "))  # Prompt for a new guess
        
    print("Congrats! The number was:", secret_number)

# Required line to call main when the script is run
if __name__ == '__main__':
    main()

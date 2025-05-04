"""
Program: favorite_animal
-------------------------
A simple Python program that asks the user for their
favorite animal and responds with a personalized message.
"""

def main():
    print("\nWhat's your favorite animal?", end=" ")
    animal = input()
    print("My favorite animal is also " + animal + "!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

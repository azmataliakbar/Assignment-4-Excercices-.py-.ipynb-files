"""
Program: Mad Libs - Adjective, Noun, Verb
-----------------------------------------
This program prompts the user for an adjective, a noun, and a verb, and then
creates a fun sentence using those inputs in a predefined sentence template.
"""

# Constant sentence beginning
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "  # adjective noun verb

def main():
    # Prompt the user for inputs
    adjective: str = input("\nPlease type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Combine and print the final sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# This line calls the main function when the script is run
if __name__ == '__main__':
    main()

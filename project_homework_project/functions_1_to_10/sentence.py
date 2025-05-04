# This program asks the user to enter a word (a noun, verb, or adjective)
# and its corresponding part of speech as a number (0 for noun, 1 for verb, 2 for adjective).
# Based on this input, it prints a sentence using the word in a relevant sentence template.

def make_sentence(word, part_of_speech):
    """
    Prints a sentence using the word based on its part of speech.
    """
    if part_of_speech == 0:
        print("\nI am excited to add this", word, "to my vast collection of them!")
    elif part_of_speech == 1:
        print("\nIt's so nice outside today it makes me want to", word + "!")
    elif part_of_speech == 2:
        print("\nLooking out my window, the sky is big and", word + "!")
    else:
        print("\nPart of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    print("\nIs this a noun, verb, or adjective?")
    part_of_speech = int(input("\nType 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

# Required to run the main function
if __name__ == '__main__':
    main()

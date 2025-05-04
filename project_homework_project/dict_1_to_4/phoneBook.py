# phonebook.py
# This program creates a simple phonebook using a dictionary.
# It allows users to enter names and numbers, print the phonebook,
# and look up numbers by name.

def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    """
    Print all name-number pairs in the phonebook.
    """
    print("\nPhonebook entries:")
    print(phonebook)  # Dictionary-style output
    for name in phonebook:
        print(f"\n{name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers by name.
    """
    print("\nPhone number lookup:")
    while True:
        name = input("\nEnter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(f"\n{name}'s number is {phonebook[name]}")
        else:
            print(f"\n{name} is not in the phonebook.")

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()

# This program prompts the user to enter elements to build a list.
# It first displays the full list entered by the user.
# Then it removes elements from the end of the list until it contains at most MAX_LENGTH items.
# It prints each removed element and finally shows the shortened list.

MAX_LENGTH: int = 3  # Maximum allowed list length

def shorten(lst):
    print("\nFull list before shortening:", lst)  # Show full list first
    
    # Remove elements until the list is no longer too long
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print("\nRemoved:", last_elem)  # Show each item removed
    
    print("\nShortened list with max length 3 elements: -> ", lst)  # Show final shortened list

# Gets list input from user
def get_lst():
    lst = []
    elem = input("\nPlease enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("\nPlease enter an element of the list or press enter to stop: ")
    return lst

# Runs the program
def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()




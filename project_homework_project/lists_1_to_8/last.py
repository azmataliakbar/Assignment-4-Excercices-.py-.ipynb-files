# This program takes a list of elements from the user (entered one by one).
# After collecting the list, it prints the last element from the list.
# The list is guaranteed to be non-empty.

def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    # Option 1: Using length - 1 since list is zero-indexed
    print("Last element of the list is: ", lst[len(lst) - 1])

    # Option 2 (also works): print("Last element:", lst[-1])

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("\nPlease enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("\nPlease enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    print("\nFull list:", lst)  # Optional: shows the full list
    get_last_element(lst)

if __name__ == '__main__':
    main()


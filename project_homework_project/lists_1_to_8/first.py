# This program collects multiple values from the user to form a list.
# After the list is formed, it prints the full list and also prints the first element in that list.

def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print("First element of the list is: ", lst[0])

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("\nPlease enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("\nPlease enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    print("\nFull list:", lst)           # 👈 This will print the whole list
    get_first_element(lst)

if __name__ == '__main__':
    main()

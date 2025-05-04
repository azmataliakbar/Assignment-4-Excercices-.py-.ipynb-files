# ----------------------------------------------------------
# Program: Count Even Numbers from User Input
# This Python program prompts the user to enter integers 
# one by one until they press Enter without typing a number.
# It stores all entered numbers in a list, displays the list,
# finds and displays all even numbers from that list,
# and finally prints the total count of even numbers.
# ----------------------------------------------------------

def count_even(lst):
    """
    Returns number of even numbers in list.
    Also prints the even numbers found.
    """
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    print("Even numbers in the list are:", even_numbers)
    return len(even_numbers)


def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []
    user_input = input("\nEnter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("\nEnter an integer or press enter to stop: ")
    return lst


def main():
    lst = get_list_of_ints()
    print("\nThe list of given integers is:", lst)
    even_count = count_even(lst)
    print("\nThe total even numbers are:", even_count)


# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()


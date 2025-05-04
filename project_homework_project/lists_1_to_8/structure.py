"""
This program demonstrates the concept of **mutability** in Python.

It defines a function `add_three_copies()` that takes a list and some data,
and adds three copies of that data to the list. The key idea is that even
though the function does not return anything, the original list gets modified
because lists are **mutable** in Python.

You’ll see the list before and after calling the function to show that the
changes persist outside the function.
"""

def add_three_copies(my_list, data):
    # Add the data to the list three times
    for _ in range(3):
        my_list.append(data)

########## No need to edit code past this point

def main():
    message = input("\nEnter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("Blank list after given range(3): ", my_list)

if __name__ == "__main__":
    main()

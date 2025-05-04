"""
This program takes a list of numbers and doubles each element.
For example, given [1, 2, 3, 4], it updates the list to [2, 4, 6, 8]
by multiplying each element by 2.
"""

def main():
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers

    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = elem_at_index * 2  # Replace it with double the value

    print("Doubled the list's number [1, 2, 3, 4]-> ", numbers)  # This prints the updated (doubled) list

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
"""
This program defines a function that takes a list of numbers
and returns the sum of those numbers. It then demonstrates the
function by summing a sample list [1, 2, 3, 4, 5] and printing the result.
"""

def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # A sample list of integers
    sum_of_numbers: int = add_many_numbers(numbers)  # Calculates the total sum
    print("\nAddition of list's numbers: ",sum_of_numbers)  # Prints the result

# This line ensures main() is only called when this file is run directly
if __name__ == '__main__':
    main()

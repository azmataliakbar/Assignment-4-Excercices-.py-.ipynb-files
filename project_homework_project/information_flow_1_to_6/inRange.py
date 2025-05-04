"""
This program defines a function `in_range(n, low, high)` that checks whether a given number `n`
is within the range defined by `low` and `high`, inclusive.
The `main()` function collects input from the user and uses the helper function to display the result.
"""

def in_range(n: int, low: int, high: int) -> bool:
    """
    Returns True if n is between low and high, inclusive.
    Assumes high is greater than low.
    """
    if low <= n <= high:
        return True
    return False

def main():
    # Get inputs from the user
    n = int(input("\nEnter a number to check: "))
    low = int(input("\nEnter the lower bound: "))
    high = int(input("\nEnter the upper bound: "))

    # Call the function and print the result
    print("\nIs the number in range?", in_range(n, low, high))

# Ensures main() runs when the file is executed
if __name__ == '__main__':
    main()

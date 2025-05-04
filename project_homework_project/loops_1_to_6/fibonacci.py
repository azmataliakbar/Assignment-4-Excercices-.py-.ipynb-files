# This Python program prints the terms in the Fibonacci sequence up to a maximum value.
# The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the previous two.
# The program continues generating terms until the value exceeds 10,000 (defined as a constant).
# It displays each term on a separate line.

MAX_TERM_VALUE: int = 10000  # Maximum value allowed for a Fibonacci term

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    
    while curr_term <= MAX_TERM_VALUE:
        print("\n",curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

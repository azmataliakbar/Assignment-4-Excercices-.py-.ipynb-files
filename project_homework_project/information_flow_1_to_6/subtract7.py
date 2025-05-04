def subtract_seven(num):
    """
    Subtracts 7 from the given number and returns the result.
    """
    num = num - 7
    return num

def main():
    num: int = 7
    num = subtract_seven(num)
    print("\nThis should be zero:", num)

# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()

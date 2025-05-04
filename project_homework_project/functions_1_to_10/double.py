# This program defines a function named `double()` that takes a number as input
# and returns the result of multiplying it by 2. The main() function prompts the
# user to enter a number, calls the double() function, and prints the doubled result.

def double(num: int):
    return num * 2

# There is no need to edit code beyond this point

def main():
    num = int(input("\nEnter a number: "))
    num_times_2 = double(num)
    print("\nDouble that is", num_times_2)

if __name__ == '__main__':
    main()

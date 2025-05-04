# This Python program prints the first 20 even numbers starting from 0.
# It uses a loop to generate even numbers by multiplying the loop index by 2.
# The output displays one even number per line and avoids manually writing multiple print statements.

def main():
    # This for-loop starts at 0 and goes up to 19 (20 numbers total)
    for i in range(20):
        print("\n", i * 2)  # Each even number is i multiplied by 2

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()


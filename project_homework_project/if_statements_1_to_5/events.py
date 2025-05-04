
# This program prints the first 20 even numbers using a loop.
# Instead of writing 20 print statements, we use a for-loop to generate and display the even numbers.

def main():
    # Loop through numbers from 0 to 19 and multiply each by 2 to get even numbers
    for i in range(20):
        print(i * 2)

# This ensures the main function runs when the script is executed
if __name__ == "__main__":
    main()

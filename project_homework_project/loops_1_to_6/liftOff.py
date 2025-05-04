# This Python program simulates a countdown for a spaceship launch.
# It prints numbers from 10 down to 1 using a loop, then prints "Liftoff!" at the end.

def main():
    for i in range(10, 0, -1):  # Start at 10, stop before 0, count down by -1
        print("\n", i)
    print("\nLiftoff!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()


# This program checks whether a given year is a leap year.
# A leap year occurs:
# - If the year is divisible by 4,
# - Except years divisible by 100 (not leap), 
# - Unless they are also divisible by 400 (leap).

def main():
    # Ask the user to enter a year
    year = int(input("\nPlease input a year: "))

    # Apply the leap year rules
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("\nThat's a leap year!")
            else:
                print("\nThat's not a leap year.")
        else:
            print("\nThat's a leap year!")
    else:
        print("\nThat's not a leap year.")

# This line calls the main() function when the script is executed
if __name__ == '__main__':
    main()

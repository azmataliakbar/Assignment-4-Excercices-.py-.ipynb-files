"""
Program: Seconds in a Year
---------------------------
This program calculates the number of seconds in a year using constants for the number of days in a year,
hours in a day, minutes in an hour, and seconds in a minute. It then prints the result in a user-friendly format.
"""

# Constants for the number of days, hours, minutes, and seconds
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # Calculate the number of seconds in a year by multiplying the constants
    seconds_in_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Print the result in a nice format
    print(f"\nThere are {seconds_in_year} seconds in a year!")

# This line calls the main() function when the script is executed
if __name__ == '__main__':
    main()

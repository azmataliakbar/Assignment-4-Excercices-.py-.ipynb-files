
# This program asks the user for their height and tells them whether or not
# they're tall enough to ride a rollercoaster. The minimum height requirement
# is set to 50 units (you can imagine it as centimeters, inches, etc.).

MINIMUM_HEIGHT: int = 50  # minimum required height to ride

def main():
    # Ask the user for their height
    height = float(input("\nHow tall are you?  "))
    
    # Check if the user meets the minimum height requirement
    if height >= MINIMUM_HEIGHT:
        print("\nYou're tall enough to ride!")
    else:
        print("\nYou're not tall enough to ride, but maybe next year!")

# This line ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()

"""
Program: Feet to Inches Converter
---------------------------------
This program converts a length from feet to inches.

It demonstrates:
- Reading user input as a float,
- Using a named constant for conversion (12 inches in 1 foot),
- Performing a simple arithmetic operation,
- Displaying the result clearly.

This is useful when working with measurements in the U.S. customary system.
"""

# Conversion constant: 1 foot = 12 inches
INCHES_IN_FOOT: int = 12

def main():
    """
    Main function that reads feet and converts to inches.
    """
    # Get input from the user
    feet: float = float(input("\nEnter number of feet: "))
    
    # Convert to inches
    inches: float = feet * INCHES_IN_FOOT

    # Print the result
    print("That is", inches, "inches!")
    print(f"That is   {inches:.2f}  inches!")
# Call the main function when this script is executed
if __name__ == '__main__':
    main()

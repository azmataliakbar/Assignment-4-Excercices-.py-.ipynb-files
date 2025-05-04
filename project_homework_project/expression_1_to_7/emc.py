"""
Program: Mass to Energy Converter
---------------------------------
This program continually reads mass input from the user in kilograms
and calculates the equivalent energy using Einstein's famous formula:

    E = m * c^2

Where:
- E is energy in joules,
- m is mass in kilograms,
- c is the speed of light in meters per second (299,792,458 m/s).

It demonstrates basic arithmetic operations, user input handling,
and the use of constants in Python.
"""

# Speed of light in meters per second (a constant)
C: int = 299_792_458

def main():
    """
    Main function to read user input for mass and compute energy.
    """
    # Read mass from the user
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's formula
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Show the computation steps and result
    print("\ne = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")
    print(f"{energy_in_joules:.2e} joules of energy!") # 6.74e+18 = 6.74 x 10¹⁸ = 6,740,000,000,000,000,000



# Call the main() function only if the script is executed directly
if __name__ == '__main__':
    main()

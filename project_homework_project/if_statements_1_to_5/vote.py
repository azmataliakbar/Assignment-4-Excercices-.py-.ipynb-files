
# This program asks the user for their age and tells them whether they can vote
# in the fictional countries of Peturksbouipo, Stanlau, and Mayengua, based on
# their respective voting age requirements.

PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

def main():
    # Ask the user for their age
    user_age = int(input("\nHow old are you? "))

    # Determine voting eligibility for each fictional country
    if user_age >= PETURKSBOUIPO_AGE:
        print("\nYou can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("\nYou cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")

    if user_age >= STANLAU_AGE:
        print("\nYou can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("\nYou cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")

    if user_age >= MAYENGUA_AGE:
        print("\nYou can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("\nYou cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")


# This line ensures the main function runs when the script is executed directly
if __name__ == '__main__':
    main()

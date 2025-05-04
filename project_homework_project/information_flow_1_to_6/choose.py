# Constant to define the legal age of adulthood
ADULT_AGE = 18  # U.S. legal age of adulthood

def is_adult(age: int):
    """
    Checks if the provided age is greater than or equal to the adult age.
    Returns True if the age is 18 or older, False otherwise.
    """
    if age >= ADULT_AGE:
        return True
    return False

def main():
    # Taking the user's input for age
    age = int(input("\nHow old is this person?: "))
    
    # Calling the is_adult function and printing the result
    print(is_adult(age))

if __name__ == '__main__':
    main()

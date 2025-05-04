# This program defines a function called `get_name()` that simply returns the name "Sophia".
# The main() function then calls get_name(), stores the result in a variable,
# and prints a friendly greeting using that name.

def get_name():
    return "Sophia"

# There is no need to edit code beyond this point

def main():
    name = get_name()  # Call get_name() and store the result
    print("\nHowdy", name, "! 🤠")  # Greet the user using the returned name

if __name__ == '__main__':
    main()

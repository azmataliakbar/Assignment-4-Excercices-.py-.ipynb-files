"""
This program defines a function `get_user_info()` that collects a user's first name,
last name, and email address through input prompts. It then returns these values as
a tuple. The `main()` function calls this helper and displays the collected data.
"""

def get_user_info():
    first_name: str = input("\nWhat is your first name?: ")
    last_name: str = input("\nWhat is your last name?: ")
    email_address: str = input("\nWhat is your email address?: ")
    
    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    user_data = get_user_info()
    print("\nReceived the following user data:", user_data)

if __name__ == "__main__":
    main()


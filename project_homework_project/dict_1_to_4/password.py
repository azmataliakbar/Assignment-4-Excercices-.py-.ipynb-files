# login_system.py
# A simple program to safely verify passwords using SHA-256 hashes without storing actual passwords.

from hashlib import sha256

# Define constants for repeated email literals
EMAIL_EXAMPLE = "example@gmail.com"
EMAIL_CIP = "code_in_placer@cip.org"
EMAIL_STUDENT = "student@stanford.edu"

def hash_password(password):
    """
    Hashes a password using SHA-256 and returns its hexadecimal digest.
    """
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hashed version of the password matches the stored hash
    for the given email. Returns False otherwise.
    """
    return stored_logins.get(email) == hash_password(password_to_check)

def main():
    # Correct SHA-256 hashes for passwords:
    # "password"       => 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
    # "karel" (lower)  => 973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc
    # "123!456?789"    => 882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb

    stored_logins = {
        EMAIL_EXAMPLE: "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
        EMAIL_CIP:     "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # karel
        EMAIL_STUDENT: "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # "123!456?789"
    }

    login_results = {
        "example@gmail.com wrong password -> (word)": login(EMAIL_EXAMPLE, stored_logins, "word"),
        "example@gmail.com correct password -> (password)": login(EMAIL_EXAMPLE, stored_logins, "password"),
        
        "code_in_placer@cip.org wrong password -> (Karel)": login(EMAIL_CIP, stored_logins, "Karel"),
        "code_in_placer@cip.org correct password -> (karel)": login(EMAIL_CIP, stored_logins, "karel"),
        
        "student@stanford.edu wrong password -> (password)": login(EMAIL_STUDENT, stored_logins, "password"),
        "student@stanford.edu correct password -> (123!456?789)": login(EMAIL_STUDENT, stored_logins, "123!456?789"),
    }

    print("\nLogin Test Results (dictionary format):")
    print("\n", login_results)

if __name__ == '__main__':
    main()

def check_password_strength(password):
    # Check if length is at least 8 characters
    if len(password) < 8:
        return False

    # Flags to check each condition
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # List of special characters to check
    special_characters = ['!', '@', '#', '$', '%']

    # Go through each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Password is strong only if all conditions are True
    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False

# Main script
if __name__ == "__main__":
    # Take input from user
    password = raw_input("Enter your password: ")

    # Check password strength
    if check_password_strength(password):
        print("Strong password! Your password meets all criteria.")
    else:
        print("Weak password. Make sure your password:")
        print("- Is at least 8 characters long")
        print("- Has both uppercase and lowercase letters")
        print("- Has at least one digit (0-9)")
        print("- Has at least one special character (!, @, #, $, %)")

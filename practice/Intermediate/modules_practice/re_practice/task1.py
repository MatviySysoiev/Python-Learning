import re


# Function to check email
def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"

    # Create new pattern for email validation
    email_check_pattern = re.compile(email_regexp)
    result = (True if email_check_pattern.fullmatch(email) else False)
    return result


# Function to check password
def check_password(password):
    lower_letters = r"[a-z]"
    upper_letters = r"[A-Z]"
    numbers = r"[0-9]"
    unique_symbol = r"[^\w\s]"

    # Check if the password meets the requirements
    if len(password) < 8:
        return False
    if not re.search(lower_letters, password):
        return False
    if not re.search(upper_letters, password):
        return False
    if not re.search(numbers, password):
        return False
    if not re.search(unique_symbol, password):
        return False

    return True


user_authorized = False

# Loop until the user is authorized
while not user_authorized:
    given_email = input("Please enter your email:\n")

    # Check if the email is valid
    if check_email(given_email):
        print("Your email was accepted!\n")
        given_password = input("Please enter your password to continue:\n")

        # Check if the password is valid
        if check_password(given_password):
            print("You have been successfully authorized!")

            # User is authorized, exit the loop
            user_authorized = True
        else:
            print("Your password is invalid. Please try again!\n\n")
    else:
        print("Your email is invalid. Please try again!\n\n")

import re
import argparse

# Initialize argument parser with a description for the script
parser = argparse.ArgumentParser(description='Password Validation using Regex')

# Add a positional argument for the password
parser.add_argument('password', type=str, help='The password to be validated')

# Parse the arguments
args = parser.parse_args()


def validate_password_regex(password):
    """
    Validate the password using a single regex pattern.
    
    The password must meet the following criteria:
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    - Minimum length of 8 characters
    
    Parameters:
    password (str): The password to be validated
    
    Returns:
    bool: True if the password is valid, False otherwise
    """
    pattern = re.compile(r'(?=.+[A-Z])(?=.+[a-z])(?=.+[0-9])(?=.+[\W])[a-zA-Z0-9\W]{8,}')
    return bool(pattern.match(password))


def validate_password_individual_checks(password):
    """
    Validate the password by checking each criterion individually.
    
    The password must meet the following criteria:
    - At least 8 characters long
    - Contains at least one lowercase letter
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special character
    
    Parameters:
    password (str): The password to be validated
    
    Returns:
    bool: True if the password is valid, False otherwise
    """
    if len(password) < 8:
        return False

    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'\W', password):
        return False
    
    return True

# Extract the password from the parsed arguments
password = args.password

# Validate the password using the individual checks method and print the result
print(validate_password_individual_checks(password))

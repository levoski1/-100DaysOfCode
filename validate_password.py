#!/usr/bin/python3
# A function that handle password validation
'''
    1. must have lenght greater than 8
    2. must have 1 uppercase letter
    3. must have atleast one number
    4. must contain a special one character
'''

from argparse import ArgumentParser



parser = ArgumentParser(description='Welcome to my code')
parser.add_argument('password',type=str)

args = parser.parse_args()

def check_password(password):
    
    # must have lenght greater than 8
    if len(password) < 8:
        return False
    
    has_upper = False
    has_digit = False
    has_alnum = False

    for num in password:
        if num.isupper():
            has_upper = True
        if num.isdigit():
            has_digit = True
        if not num.isalnum():
            has_alnum = True

    if not(has_alnum and has_digit and has_upper):
        return False
    
    
    return True


print(check_password(args.password))

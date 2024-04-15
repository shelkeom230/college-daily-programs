# Write a program that validates a user's password based on the following criteria (in the following order):
# 1. The password must be at least 8 characters long.
# 2. The password must contain at least one uppercase letter (A-Z).
# 3. The password must contain at least one lowercase letter (a-z).
# 4. The password must contain at least one digit (0-9).

# Take the following assumptions regarding the input:
# The input will not contain any spaces

# Your output should print the rule that it violates exactly as defined above.

# If the password violates multiple rules then the first rule it violates should take priority

# Example - 
# Input - pass
# Output - 
# Your password is invalid.
# The password must be at least 8 characters long

def checkPass(password):
    length=len(password)
    if length<8:
        print('Your password is invalid\npassword must be at least 8 chars long')
    elif not any(char.isupper() for char in password):
        print('Your password is invalid\npassword must have at least 1 uppercase letter')
    elif not any(char.islower() for char in password):
        print('Your password is invalid\npassword must have at least 1 lowercase letter')
    elif not any(char.isdigit() for char in password):
        print('Your password is incorrect\npassword must have atleasst one number.')
    else:
        print("your password is ok")        

import re as r
def checkPassword2(password):
    if len(password)<8:
        print("invalid password\n must have length greater than or equal to 8")
    elif not r.search(f'[A-Z]',password): print("invalid password\nmust have 1 uppercase")
    elif not r.search(f'[a-z]',password): print("invalid password\nmust have atleast one lowercase letter")
    elif not r.search(f'\d',password): print("invalid password\nmust have atleast 1 number brother")
    else: print("corrrect")
             
checkPass('om')                          
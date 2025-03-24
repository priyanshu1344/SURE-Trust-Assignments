import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'
    return bool(re.match(pattern, email))

email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")

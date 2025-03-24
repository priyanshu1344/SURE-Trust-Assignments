import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'
    return bool(re.match(pattern, email))

email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")

# print(is_valid_email("student@example.com"))  # Expected Output: True
# print(is_valid_email("user.name@my-site.org"))  # Expected Output: True
# print(is_valid_email("invalid-email.com"))  # Expected Output: False
# print(is_valid_email("missing@domain"))  # Expected Output: False
# print(is_valid_email("@nouser.com"))  # Expected Output: False

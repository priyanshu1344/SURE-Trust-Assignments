import re

def is_only_letters(text):
    return bool(re.fullmatch(r'[A-Za-z]+', text))

text = input("Enter a string: ")
print("true" if is_only_letters(text) else "False")



# print(is_only_letters("HelloWorld"))  # Expected Output: True
# print(is_only_letters("Hello123"))    # Expected Output: False
# print(is_only_letters("Python!"))     # Expected Output: False

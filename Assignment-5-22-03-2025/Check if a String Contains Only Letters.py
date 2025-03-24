import re

def is_only_letters(text):
    return bool(re.fullmatch(r'[A-Za-z]+', text))

text = input("Enter a string: ")
print("true" if is_only_letters(text) else "False")

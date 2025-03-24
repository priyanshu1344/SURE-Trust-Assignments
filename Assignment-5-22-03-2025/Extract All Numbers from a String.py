import re

def extract_numbers(text):
    return re.findall(r'\d+', text)

text = input("Enter a string: ")
print("Extracted numbers:", extract_numbers(text))


# print(extract_numbers("I have 2 apples and 15 oranges."))  # ['2', '15']
# print(extract_numbers("No numbers here!"))  # []
# print(extract_numbers("Room 404 is not found, but 808 is available."))  # ['404', '808']
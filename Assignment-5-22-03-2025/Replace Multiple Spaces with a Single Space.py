import re

def normalize_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

text = input("Enter a sentence: ")
print("Cleaned text:", normalize_spaces(text))

import re

def find_ing_words(text):
    return re.findall(r'\b\w+ing\b', text)

text = input("Enter a sentence: ")
print("Words ending with 'ing':", find_ing_words(text))

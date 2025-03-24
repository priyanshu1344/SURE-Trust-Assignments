import re

def find_ing_words(text):
    return re.findall(r'\b\w+ing\b', text)

text = input("Enter a sentence: ")
print("Words ending with 'ing':", find_ing_words(text))




# print(find_ing_words("I am running and she is singing."))  # Expected Output: ['running', 'singing']
# print(find_ing_words("Walking is fun but jumping is better!"))  # Expected Output: ['Walking', 'jumping']
# print(find_ing_words("No ING words here!"))  # Expected Output: []

import re

def normalize_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

text = input("Enter a sentence: ")
print("Cleaned text:", normalize_spaces(text))



# print(normalize_spaces("This   sentence   has    too   many spaces."))  # Expected Output: "This sentence has too many spaces."
# print(normalize_spaces("No extra spaces here."))  # Expected Output: "No extra spaces here."
# print(normalize_spaces("     Leading and trailing spaces should be removed too.    "))  # Expected Output: "Leading and trailing spaces should be removed too."

#Question 5: Check if a String is Pangram 
#You are designing a chatbot for an e-commerce platform. The chatbot is expected to understand and respond to user queries efficiently. To ensure that it can handle diverse inputs, you need to verify that its internal processing covers all possible alphabetical characters. A pangram is a sentence that contains every letter of the English alphabet at least once. 
#Write a Python function that takes a string as input and checks whether the string is a pangram (contains every letter of the alphabet at least once). 


def is_pangram(sentence):
    letters_found = {char.lower() for char in sentence if char.isalpha()}
    return len(letters_found) == 26

sentence = input("Enter a sentence: ")
print(is_pangram(sentence))

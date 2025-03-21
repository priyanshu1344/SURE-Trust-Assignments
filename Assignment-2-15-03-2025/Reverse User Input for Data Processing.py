#Question 2: Reverse User Input for Data Processing 
#Imagine you are developing a secure system for user input validation, and part of the system involves reversing strings (such as passwords or IDs) for a unique encryption method. 
#Write a Python program that accepts a string from the user and returns it in reverse order. This could simulate part of a process where data is transformed before being stored or transmitted securely.



def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

user_input = input("Enter a string to reverse: ")
print("Reversed string:", reverse_string(user_input))

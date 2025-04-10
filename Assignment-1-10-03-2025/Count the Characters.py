#Question 1: Count the Characters 
#Imagine you are developing a text analysis tool for a messaging app. One of the features you want to implement is the ability to count how often each character (letters, digits, spaces, and punctuation marks) appears in a given message.
#Your task is to write a simple Python program that takes a message from the user and counts the frequency of each character, including letters, digits, spaces, and special characters. 



def count_characters(message):
    char_count = {}
    for char in message:
        if char in char_count: 
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

message = input("Enter a message: ")
print(count_characters(message))

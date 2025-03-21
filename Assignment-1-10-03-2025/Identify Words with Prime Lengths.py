#Question 3: Identify Words with Prime Lengths 
#Imagine you're helping a teacher grade a language test. In one of the tasks, students were asked to identify and list all the words from a passage that have a length equal to a prime number. Your task is to write a Python program that does this automatically. 
#The program will take a sentence or passage as input and output all the words whose length is a prime number.



def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def identify_prime_length_words(sentence):
    words = sentence.split()
    result = []
    for word in words:
        clean_word = ''.join(filter(str.isalpha, word))  # Remove punctuation
        if is_prime(len(clean_word)):
            result.append(clean_word)
    return ' '.join(result)

sentence = input("Enter a sentence: ")
print(identify_prime_length_words(sentence))

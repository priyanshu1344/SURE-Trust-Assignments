#Question 2: Race for the Armstrong Award 
#In a maths competition, the Armstrong award would be presented to the one who would first tell the Armstrong number among all given numbers. Thus, write a program for Sam in Python to help him won the award. 


def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    total = 0
    for d in digits:
        total += d ** power
    return total == number

number = int(input("Enter a number: "))
print("Number is Armstrong" if is_armstrong(number) else "Number is not Armstrong")

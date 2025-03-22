class UnderageError(Exception):
    pass

def verify_age(age):
    if age < 18:
        raise UnderageError("Access Denied: You must be at least 18.")
    print("Access Granted")

try:
    age = int(input("Enter your age: "))
    verify_age(age)
except ValueError:
    print("Invalid Input! Age must be a number.")
except UnderageError as e:
    print(e)


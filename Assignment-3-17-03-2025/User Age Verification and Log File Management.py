
class UnderageError(Exception):
    """Exception raised when a user is under 18."""
    pass

def verify_age(age):
    if age < 18:
        raise UnderageError(f"Access Denied: You must be at least 18 years old. (Your age: {age})")
    print(f"Access Granted! (Your age: {age}) Welcome!")

def log_error(error_message):
    try:
        with open("error.log", "a") as file:
            file.write(error_message + "\n")
        print(" Error logged successfully.")
    except IOError:
        print(" Error: Could not write to log file.")

try:
    age = int(input(" Enter your age: "))
    verify_age(age)
except ValueError:
    error_msg = " Invalid Input: Age must be a number."
    print(error_msg)
    log_error(error_msg)
except UnderageError as e:
    print(e)
    log_error(str(e))
except Exception as e:
    print(f" Unexpected error: {e}")
    log_error(str(e))

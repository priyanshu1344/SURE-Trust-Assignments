
def calculate_average(marks):
    if not marks:
        raise ValueError(" Error: The marks list is empty. Please provide valid marks.")
    if not all(isinstance(mark, (int, float)) for mark in marks):
        raise TypeError(" Error: All marks must be numbers.")

    average = sum(marks) / len(marks)
    return average

def save_marks_to_file(filename, marks):
    try:
        with open(filename, "w") as file:
            file.write(",".join(map(str, marks)))
        print(f"Marks saved to {filename}.")
    except IOError:
        print(" Error: Could not write to file. Please check file permissions.")

def read_marks_from_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read().strip()
            if not data:
                raise ValueError(" Error: The file is empty.")
            
            marks = list(map(int, data.split(",")))
            return marks
    except FileNotFoundError:
        print(f" Error: File '{filename}' not found. Please save marks first.")
    except ValueError:
        print(" Error: The file contains invalid data. Expected numbers only.")
    return []

marks = []
while True:
    try:
        mark = input(" Enter a student's mark (or type 'done' to finish): ")
        if mark.lower() == "done":
            break
        marks.append(int(mark))
    except ValueError:
        print(" Invalid input! Please enter a number.")

try:
    avg = calculate_average(marks)
    print(f"\n Average Marks: {avg:.2f}")
    filename = "student marks"
    save_marks_to_file(filename, marks)
    print("\n Reading marks back from file...")
    read_marks = read_marks_from_file(filename)
    print(f" Read Marks: {read_marks}")
except Exception as e:
    print(f" Unexpected error: {e}")

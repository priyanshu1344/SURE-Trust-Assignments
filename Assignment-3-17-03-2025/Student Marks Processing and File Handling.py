def calculate_average(marks):
    if not marks:
        return "No marks provided."
    return sum(marks) / len(marks)

def save_marks(filename, marks):
    with open(filename, "w") as file:
        file.write(",".join(map(str, marks)))
    print(f"Marks saved to {filename}")

def read_marks(filename):
    try:
        with open(filename, "r") as file:
            return list(map(int, file.read().split(",")))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

marks = []

while True:
    mark = input("Enter a mark (or 'done' to finish): ")
    if mark.lower() == "done":
        break
    try:
        marks.append(int(mark))
    except ValueError:
        print("Invalid input! Enter a number.")

if marks:
    avg = calculate_average(marks)
    print(f"\nAverage Marks: {avg:.2f}")
    filename = "marks.txt"
    save_marks(filename, marks)
    print("\nReading marks from file...")
    print("Read Marks:", read_marks(filename))


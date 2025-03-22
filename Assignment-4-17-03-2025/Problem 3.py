# class Time:
#     def __init__(self, h, m):
#         self.h = h
#         self.m = m

#     def display_time(self):
#         if self.h >= 24:
#             print("Hours should be < 24.")
#             return
#         if self.m >= 60:
#             print("Minutes should be < 60.")
#             return
        
#         am_pm = "AM" if self.h < 12 else "PM"
#         hour = self.h % 12 or 12
#         print(f"{hour}:{self.m:02d} {am_pm}")

#     def display_ratio(self):
#         try:
#             print(f"Ratio: {self.m / self.h:.2f}")
#         except ZeroDivisionError:
#             print("Ratio can't be calculated.")

# h = int(input("Hours: "))
# m = int(input("Minutes: "))

# t = Time(h, m)
# t.display_time()
# t.display_ratio()





class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def display_time(self):
        if self.h >= 24:
            print("Invalid hours!")
            return
        if self.m >= 60:
            print("Invalid minutes!")
            return
        
        am_pm = "AM" if self.h < 12 else "PM"
        hour = self.h % 12 or 12
        print(f"{hour}:{self.m:02d} {am_pm}")

    def display_ratio(self):
        try:
            print(f"Ratio: {self.m / self.h:.2f}")
        except ZeroDivisionError:
            print("Can't divide by zero!")

times = [(23, 45), (34, 50), (12, 34), (14, 67), (19, 20), (2, 15), (0, 10)]

for h, m in times:
    t = Time(h, m)
    t.display_time()
    t.display_ratio()

#Question 1: Calculate Euclidean distance 
#Write a Python program to calculate Euclidean Distance. 


def euclidean_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

x1, y1 = map(float, input("Enter first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter second point (x2 y2): ").split())

print(f"The Euclidean Distance is: {euclidean_distance(x1, y1, x2, y2)}")

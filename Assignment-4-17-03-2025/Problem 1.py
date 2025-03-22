import math

class Cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def volume(self):
        return math.pi * self.r ** 2 * self.h

    def surface_area(self):
        return 2 * math.pi * self.r * self.h

r = float(input("Radius: "))
h = float(input("Height: "))

cyl = Cylinder(r, h)
print(f"Volume: {cyl.volume():.2f}")
print(f"Surface Area: {cyl.surface_area():.2f}")

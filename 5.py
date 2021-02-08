from math import pi
def C_V(r, h):
    print("Circumference is :", 2 * pi * r)
    print("Volume is :", pi * r**2 * h)
r = int(input("Enter the radius"))
h = int(input("Enter the heigth"))
C_V(r, h)

"""A module of functions related to circles."""
import math

##########DONT######
a=1


def area(radius,arg_a):
    """Returns the area of a circle given its radius."""
   
    return math.pi * radius**2*arg_a

def circumference(radius):
    """Returns the circumference of a circle given its radius."""
    return 2 * math.pi * radius


if __name__ == '__main__':
    # Simple sanity checks
    print("hellp")
    print("Area of circle of radius 3:", area(3,a))
    print("Circumference of circle of radius 3:", circumference(3))

# print("@@@@@@@@Area of circle of radius 3:", area(3))
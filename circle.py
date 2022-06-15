""""
Author: O. Smit

Description:

Uses one value (representing either area, circumference, or radius)
to calculate the two missing values. These results are printed
for the user. The necessary equations are imported from 'formules.py'.
"""
from sys import argv
from formules import CirkelFormules


class Circle(object):

    def __init__(self, radius=None, circumference=None, area=None):
        self.r = radius
        self.C = circumference
        self.A = area

    def get_radius(self):
        if self.C is not None:
            return round(CirkelFormules.r_from_C(float(self.C)), 3)
        elif self.A is not None:
            return round(CirkelFormules.r_from_A(float(self.A)), 3)
        else:
            raise Exception("Cannot compute radius.")

    def get_circumference(self):
        if self.r is not None:
            return round(CirkelFormules.C_from_r(float(self.r)), 3)
        elif self.A is not None:
            return round(CirkelFormules.C_from_A(float(self.A)), 3)
        else:
            raise Exception("Cannot compute circumference.")

    def get_area(self):
        if self.r is not None:
            return round(CirkelFormules.A_from_r(float(self.r)), 3)
        elif self.C is not None:
            return round(CirkelFormules.A_from_C(float(self.C)), 3)
        else:
            raise Exception("Cannot compute area.")


if float(argv[2]) >= 0:

    if argv[1] == 'radius=':
        object = Circle(radius=argv[2])
        circumference = object.get_circumference()
        area = object.get_area()
        print(f"Circumference: {circumference}\nArea: {area}")

    elif argv[1] == 'circumference=':
        object = Circle(circumference=argv[2])
        radius = object.get_radius()
        area = object.get_area()
        print(f"Radius: {radius}\nArea: {area}")

    elif argv[1] == 'area=':
        object = Circle(area=argv[2])
        radius = object.get_radius()
        circumference = object.get_circumference()
        print(f"Radius: {radius}\nCircumference: {circumference}.")

    else:
        raise Exception("Input unclear. Try again. E.g.: circle.py radius= 20")
else:
    raise Exception("Cannot be a negative number.")

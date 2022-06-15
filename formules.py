"""
Author: O. Smit

Description:

A collection of equations for different shapes
to be exported and used in other files.
"""


from math import pi
from math import sqrt


class CirkelFormules(object):

    def A_from_C(circumference):
        area = circumference**2 / (4 * pi)
        return area

    def A_from_r(radius):
        area = pi * radius**2
        return area

    def C_from_A(area):
        circumference = 2 * sqrt(area * pi)
        return circumference

    def C_from_r(radius):
        circumference = 2 * pi * radius
        return circumference

    def r_from_A(area):
        radius = sqrt(area / pi)
        return radius

    def r_from_C(circumference):
        radius = circumference / (2 * pi)
        return radius


class ZeshoekFormules(object):

    def C_from_S(sidelength):
        circumference = 6 * sidelength
        return circumference

    def A_from_S(sidelength):
        area = (3 * sqrt(3) * sidelength**2) / 2
        return area

import math


def area_of_ellipse(minor_length, major_length):
    area_of_ell = math.pi * minor_length * major_length
    return area_of_ell


a = float(input('enter the minor length:'))
b = float(input('enter the major length:'))
print(area_of_ellipse(a, b))

import math


def circle_area(rad):
    area = math.pi * math.pow(rad, 2)
    return area


def circumference_of_circle(rad):
    circum = 2 * math.pi * rad
    return circum


radius = float(input('enter the radius of the circle: '))
print(circle_area(radius))
print(circumference_of_circle(radius))

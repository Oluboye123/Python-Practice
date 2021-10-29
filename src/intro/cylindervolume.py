import math


def area_of_cylinder(rad, height):
    area = 2 * math.pi * rad * (rad + height)
    return area


def volume_of_cylinder(rad, height):
    volume = math.pi * math.pow(rad, 2) * height
    return volume


cyl_height = float(input('enter the height of the cylinder:'))
cyl_radius = float(input('enter the radius of the cylinder:'))

print(area_of_cylinder(cyl_radius, cyl_height))
print(volume_of_cylinder(cyl_radius, cyl_height))

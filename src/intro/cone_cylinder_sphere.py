# pi is a contant variable 
pi = 3.1416


# A function that calculate the volume of a sphere
def sphere(r):
    v = (4 * (pi) * (r**3)) / 3             # Using formula for the volume of a sphere
    return v


# A function that calculate the volume of a cylinder
def cylinder(r, l):
    v = pi * (r**2) * l                     # Using formula for the volume of a cylinder
    return v


# A function that calculate the volume of a cone
def cone(r, l):
    v = (pi * (r**2) * l) / 3               # Using formula for the volume of a cone
    return v


# Call the functions to get the volumes of sphere, cylinder, cone and print the volumes
print(sphere(3))
print(cylinder(2,3))
print(cone(2,3))
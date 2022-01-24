pi = 3.1416

import math  

# A function that calculate the area of a sphere
def sphere():
    r = float(input("Please enter the radius of the sphere: "))
    a = 4 * pi * (r**2)
    print("The area of the sphere is ", a)
    
# A function that calculate the area of a cylinder
def cylinder():
    r = float(input("Please enter the radius of the cylinder: "))
    h = float(input("Please enter the height of the cylinder: "))
    a = (2 * pi * r * h) + (2 * pi * (r**2))
    print("The area of the cylinder is ", a)
    
# A function that calculate the area of a cone
def cone():
    r = float(input("Please enter the radius of the cone: "))
    h = float(input("Please enter the height of the cone: "))
    a = pi * r * (r + math.sqrt((h**2)+(r**2)))                # The sqrt() method returns the square root of any number
    print("The area of the cone is ", a)
    
#Ask the question again using recursion
def menu():
    press = input("Which shape you would like to calculate the area of? \nPlease type 1 for sphere, 2 for cylinder and 3 for cone: ")
    
    if press == "1":
        sphere()
    elif press == "2":
        cylinder()
    elif press == "3":
        cone()
    else:
        menu()

#Call the menu function to start the program
menu()


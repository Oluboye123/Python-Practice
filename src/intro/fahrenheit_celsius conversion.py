def fahrenheit_to_celsius(temp_in_fahrenheit):
    temp_in_celsius = (temp_in_fahrenheit - 32) * 5/9
    return temp_in_celsius


def celsius_to_fahrenheit(temp_in_celsius):
    temp_in_fahrenheit = (temp_in_celsius * 9/5) + 32
    return temp_in_fahrenheit


temp_in_cels = float(input('enter the temp in celsius: '))
print(celsius_to_fahrenheit(temp_in_cels), "fahrenheit")

temp_in_fahren = float(input('enter the temp in fahrenheit: '))
print(fahrenheit_to_celsius(temp_in_fahren), "degree celsius")

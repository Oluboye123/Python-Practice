def sum(x: int, y: int, z: int):
    addition = x + y + z
    return addition


first_num = input("first number")
second_num = input("second number")
third_num = input("third number")

print(sum(int(first_num), int(second_num), int(third_num)))


def product(x: int, y: int, z: int):
    multiply = x * y * z
    return multiply


def average(x: int, y: int, z: int):
    avg = sum(x, y, z)/3
    return avg


print(product(int(first_num), int(second_num), int(third_num)))
print(sum(int(first_num), int(second_num), int(third_num)))
print(average(int(first_num), int(second_num), int(third_num)))

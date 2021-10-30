def sorting(x: int, y: int, z: int):
    number = [x, y, z]
    sorted_num = sorted(number)
    return sorted_num


first_num = int(input('enter first number: '))
second_num = int(input('enter a second number:'))
third_num = int(input('enter a third number: '))

print(sorting(first_num, second_num, third_num))

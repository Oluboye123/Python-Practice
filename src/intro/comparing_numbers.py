def compare_numbers(x: int, y: int):
    if x > y:
        print(first_num, "is greater than", second_num)
    elif x < y:
        print(second_num, "is greater than", first_num)
    else:
        print('Same numbers')


first_num = int(input('enter first integer: '))
second_num = int(input('enter second integer: '))
compare_numbers(first_num, second_num)

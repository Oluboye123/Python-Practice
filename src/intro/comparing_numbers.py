def compare_numbers(x: int, y: int):
    if first_num > second_num:
        print(first_num, "is greater than", second_num)
    elif first_num < second_num:
        print(second_num, "is greater than", first_num)
    else:
        print('Same numbers')


first_num = int(input('enter first integer: '))
second_num = int(input('enter second integer: '))
compare_numbers(first_num, second_num)

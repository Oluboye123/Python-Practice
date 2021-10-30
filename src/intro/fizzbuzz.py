def fizz_buzz(x: int):
    if x % 5 == 0 and x % 3 == 0:
        print("FIZZ BUZZ")
    elif x % 5 == 0:
        print("BUZZ")
    elif x % 3 == 0:
        print("FIZZ")
    else:
        print(number, "is not divisible by both 3 and 5")


number = int(input('Enter a number: '))
fizz_buzz(number)

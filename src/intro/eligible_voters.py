def eligible_voters(name, age, country):
    if age < 18:
        print(name, "You are not eligible to vote")
    elif age > 18 and country == "UK" or "BRITAIN":
        print(name, 'You are eligible to vote. Kindly proceed')
    elif age > 18 and country != "UK" or "BRITAIN":
        print(name, 'You are not entitled to vote')
    else:
        print(name, 'Thank you for coming, you are not voting')


voters_name = input("what is your name?: ")
voters_age = int(input("what is the age of the voter?: "))
voters_country_of_citizenship = input("where is the voters country?: ")


eligible_voters(voters_name, voters_age, voters_country_of_citizenship)

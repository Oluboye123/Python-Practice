import random

# 1 dice has 6 sides - 1,2,3,4,5,6
# 2 dice have (6+6) = 12 sides 
# we get 2,3,4,5,6,7,8,9,10,11,12 from 2 dice

def dice(n):
    return [random.randint(1, 6) + random.randint(1, 6) for _ in range(n)]    # get the thrown value of 2 dice

rollList = dice(100)                                                              # throw 2 dice 100 times
print(rollList)

#Record how often each number from 2 to 12 is thrown in a suitable list

occurrenceList = []

for i in range(2,13):
    occurrenceList.append(rollList.count(i))    # Count the occurrence of each number from 2 to 12
    
print(occurrenceList)

#print out a graph

print("Distribution Chart")
print("Score\t\tRolls")

for i in range(2,13):
    print(i, "\t\t", occurrenceList[i-2], "\t\t",str("*"*occurrenceList[i-2]).ljust(20," "))

    


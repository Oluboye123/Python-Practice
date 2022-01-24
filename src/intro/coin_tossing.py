import random

#Toss
coins = ['H','T']
dataList = []
for i in range(100):
    dataList.append(random.choice(coins)) 
    # randomly choice "H" or "T" and store the value in a list named dataList
print(dataList)

#print out the list in 5 rows of 20.
start = 0
end = 20
for i in range(5):                                # loop for row counter
    for j in range(start,end):                    # loop for 20 data in a row
        print(dataList[j],end="  ")
    print("\n")                                   # print new line
    start = start+20                              # increase the value 20 in each loop to get next values
    end = end+20                                  # increase the value 20 in each loop to get next values

#find the longest continuous run of heads and the longest continuous run of tails
def LongestRun(tossList, lookFor):
    current_longest = 0
    max_longest = 0
    for x in tossList:
        if x == lookFor:
            current_longest+=1
            if current_longest > max_longest:
                max_longest = current_longest
        else:
            current_longest=0
    return max_longest

print("Longest Continuous Run of Heads: ",LongestRun(dataList,'H'))
print("Longest Continuous Run of Tails: ",LongestRun(dataList, 'T'))   

#count how many times three heads were tossed in a row

counterHead = 0
c = 0
start = 0
end = 20
for i in range(5):                                # loop for row counter
    for j in range(start,end):                    # loop for 20 data in a row
        print(dataList[j],end="  ")
        if dataList[j] == 'H':
            c +=1
            if c == 3:
                counterHead += 1
                c = 0
        else:
            c = 0
    print("\tCounter Head (3 Consequtive Heads in a Row): ", counterHead)

    print("\n")                                   # print new line
    start = start+20                              # increase the value 20 in each loop to get next values
    end = end+20                                  # increase the value 20 in each loop to get next values
    counterHead = 0
    c = 0


import random

#Generate 20 random numbers between 0 and 99
randomList = random.sample(range(0, 99), 20)
print(randomList)

#Locate second largest and smallest numbers
randomList.sort()
print(randomList)
secondLargest = randomList[-2]
secondSmallest = randomList[1]

print("Second Largest number is: ", secondLargest)
print("Second Smallest number is: ", secondSmallest)

#remove all entries greater than the third highest number
randomList = random.sample(range(0,99), 20)
newList = randomList.copy()
print("New Random List: ", randomList)
randomList.sort()
thirdHighest = randomList[-3]
print("Third Highest number is: ", thirdHighest)

removeList = []
for num in randomList:    
    if num > thirdHighest:
        removeList.append(num)

for r in removeList:
    newList.remove(r)
        
print("The resulting list is: ", newList)

# Create new Random List and insert 50 in the middle position in the list
newRandomList = random.sample(range(0,99),20)
print("New Random List: ", newRandomList)

#find out middle position in the list
mid_index = len(newRandomList)//2 

newRandomList.insert(mid_index, 50)                       
# insert 50 in the middle position in the list

print("New Random List after insert 50 in the middle index: ",newRandomList)


#All numbers in the first half of the list that are greater than 50 are removed from the first half and appended to the second half.
tempList = []
for i in range(0, mid_index):
    if newRandomList[i] > 50:
        tempList.append(newRandomList[i])

for i in tempList:
    newRandomList.remove(i)
    newRandomList.append(i)
    
print("The final output of the list: ", newRandomList)

#All numbers in the second half of the list that are smaller than 50, appending them to the end of the first half of the list before the number 50

index_fifty = mid_index - len(tempList)  # identify index of fifty to Get the second half of the previous list 
print("Index of fifty: ", index_fifty)
tempList2 = []

for i in range(index_fifty+1, len(newRandomList)):
    if newRandomList[i] < 50:
        tempList2.append(newRandomList[i])

print(tempList2)

for i in tempList2:
    newRandomList.remove(i)
    newRandomList.insert(index_fifty,i)

print("The final output of the list: ", newRandomList)




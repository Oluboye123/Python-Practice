from random import *
rucksack = ["Water flask","Cheese","Gold coins","Handkerchief","Tinderbox","Scrolls","Dagger","Rope","Nuts","Pipe","Tobacco","Wine skin","Herbs","Axe"]
rucksack.sort()
print(rucksack)

print("Number of items in rucksack is ",len(rucksack))

rucksack.append("gems")
rucksack.append("necklace")

rucksack.sort()
print(rucksack)

steal_items = sample(rucksack,  5)   # Pick 5 random items from the list
for s_item in steal_items:
    rucksack.remove(s_item)
print(steal_items)
print(rucksack)

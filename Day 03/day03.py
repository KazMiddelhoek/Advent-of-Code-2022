f = open("Day 03\input.txt","r")
rucksacks = f.read().splitlines()

def get_priority(item):
    if item.islower():
        return (ord(item)-96)
    else:
        return (ord(item)-38)

sum_priorities = 0
for rucksack in rucksacks:
    item=([item for item in rucksack[:int(len(rucksack)/2)] if item in rucksack[int(len(rucksack)/2):]])[0]
    sum_priorities+=get_priority(item)
print(sum_priorities)

# part 2
total_badges=0
for i in range(0,len(rucksacks),3):
    group=rucksacks[i:i+3]
    badge=[item for item in group[0] if item in group[1] and item in group[2]][0]
    total_badges+=get_priority(badge)
print(total_badges)

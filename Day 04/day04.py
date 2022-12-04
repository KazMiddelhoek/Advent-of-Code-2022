f = open("Day 04\input.txt","r")
pairs = f.read().splitlines()

n_fully_overlapping_pairs=0
for pair in pairs:
    numbers=pair.replace("-",",").split(",")
    numbers=[int(number) for number in numbers]
    if (numbers[0]<=numbers[2] and numbers[1]>=numbers[3]) or (numbers[0]>=numbers[2] and numbers[1]<=numbers[3]):
        n_fully_overlapping_pairs+=1
print(n_fully_overlapping_pairs)

# part 2
n_overlapping_pairs=0
for pair in pairs:
    numbers=pair.replace("-",",").split(",")
    numbers=[int(number) for number in numbers]
    if set(range(numbers[0],numbers[1]+1)).intersection(set(range(numbers[2],numbers[3]+1))):
        n_overlapping_pairs+=1
print(n_overlapping_pairs)

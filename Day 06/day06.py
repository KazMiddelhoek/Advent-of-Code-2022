f = open("Day 06\input.txt","r")
datastream = f.read()

for i in range(4,len(datastream)):
    if len(set(datastream[i-4:i]))==4:
        print(i)
        break

# part 2
for i in range(14,len(datastream)):
    if len(set(datastream[i-14:i]))==14:
        print(i)
        break
f = open("Day 01\input.txt","r")
lines = f.read().splitlines()

input_list=[]
elf=[]
for line in lines:
    if line=="":
        input_list.append(elf)
        elf=[]
    else:
        elf.append(int(line))


sums=[sum(elf) for elf in input_list]
max_sum=max(sums)
print(max_sum)

#part 2
print(sum(sorted(sums,reverse=True)[:3]))
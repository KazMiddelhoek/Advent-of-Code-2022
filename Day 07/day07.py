f = open("Day 07\input.txt","r")
lines = f.read().splitlines()

#Find size in each directory
filesystem={}
current_dir=""
for line in lines:
    if line[:4]=="$ cd":
        if line[5]=="/":
            current_dir="/"
        elif line[5:7]=="..":
            current_dir=current_dir[:current_dir[:-1].rfind("/")+1]    
        else:
            current_dir+=line[5:]+"/"
    elif line[:4]=="$ ls":
        filesystem[current_dir]=0
    elif line[:3]!="dir":
        filesystem[current_dir]+=int(line.split(" ")[0])

#Add sizes of subdirectories to directories above
total_filesystem={}
for key in filesystem:
    total_filesystem[key]= sum([filesystem[subkey] for subkey in [subkey for subkey in filesystem if key in subkey]])

print(sum([value for value in total_filesystem.values() if value <= 100000]))

#part 2
print(min([value for value in total_filesystem.values() if value >= (total_filesystem["/"]-40_000_000)]))
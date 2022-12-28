f = open("Day 23\input.txt","r")
map=f.read().splitlines()

def get_elves(map):
    elves=[]
    for line in range(len(map)):
        for x in range(len(map[0])):
            if map[line][x]=="#":
                elves.append((x,line))
    return elves

def print_elves(elves):
    print(" ")
    x_range=[min(elves,key=lambda x: x[1])[1],max(elves,key=lambda x: x[1])[1]]
    y_range=[min(elves,key=lambda x: x[0])[0],max(elves,key=lambda x: x[0])[0]]
    for i in range(x_range[0],x_range[1]+1):
        for j in range(y_range[0],y_range[1]+1):
            if (j,i) in elves:
                print("#",end="")
            else:
                print(".",end="")
        print("")

def look_around(point):
    return [(point[0]-1,point[1]-1),
    (point[0],point[1]-1),
    (point[0]+1,point[1]-1),
    (point[0]+1,point[1]),
    (point[0]+1,point[1]+1),
    (point[0],point[1]+1),
    (point[0]-1,point[1]+1),
    (point[0]-1,point[1]),]

def look_north(point):
    return [
        (point[0]-1,point[1]-1),
        (point[0],point[1]-1),
        (point[0]+1,point[1]-1),]

def look_east(point):
    return [
        (point[0]+1,point[1]-1),
        (point[0]+1,point[1]),
        (point[0]+1,point[1]+1),
    ]

def look_south(point):
    return [
        (point[0]-1,point[1]+1),
        (point[0],point[1]+1),
        (point[0]+1,point[1]+1),
    ]

def look_west(point):
    return [
        (point[0]-1,point[1]-1),
        (point[0]-1,point[1]),
        (point[0]-1,point[1]+1),
    ]

look_directions=[look_north,look_south,look_west,look_east]

elves=get_elves(map)
for round in range(10):
    new_positions=[]
    for i in range(len(elves)):
        loc_found=False
        if any(loc in elves for loc in look_around(elves[i])):
            for func in look_directions[round%4:]+look_directions[:round%4]:
                new_locs=func(elves[i])
                if not any(loc in elves for loc in new_locs):
                    new_positions.append(new_locs[1])
                    loc_found=True
                    break
        if not loc_found:
            new_positions.append(elves[i])

    # now try moving
    not_moveable_positions=list(set([pos for pos in new_positions if new_positions.count(pos) > 1]))
    for i in range(len(new_positions)):
        if new_positions[i] in not_moveable_positions:
            new_positions[i]=elves[i]
    elves=new_positions

# calc square
print(
    (max(elves,key=lambda x: x[0])[0]+1-min(elves,key=lambda x: x[0])[0])*(max(elves,key=lambda x: x[1])[1]+1-min(elves,key=lambda x: x[1])[1])
    - len(elves)
)

# part 2
round=0
elves=set(get_elves(map))
elves={elf: None for elf in elves}
while True:
    for elf in elves:
        loc_found=False
        if any(loc in elves for loc in look_around(elf)):
            for func in look_directions[round%4:]+look_directions[:round%4]:
                new_locs=func(elf)
                if not any(loc in elves for loc in new_locs):
                    elves[elf]=new_locs[1]
                    loc_found=True
                    break
        if not loc_found:
            elves[elf]=elf

    # now try moving
    to_move=elves.values()
    not_moveable_positions=set([pos for pos in to_move if list(to_move).count(pos) > 1])
    new_positions={elf: (elf if elves[elf] in not_moveable_positions else elves[elf]) for elf in elves}
    round+=1
    if all(curr==prop for curr,prop in new_positions.items()):
        break
    elves={elf: None for elf in new_positions.values()}
print(round+1)
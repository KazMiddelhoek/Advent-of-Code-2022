f = open("Day 22\input.txt","r")
map=f.read().splitlines()
instructions = map[-1]
instructions=instructions.replace("R"," R ").replace("L", " L ").split(" ")
instructions=[int(instr) if instr!="L" and instr!="R" else instr for instr in instructions]
map=map[:-2]
rocks=set()
valid_positions=set()
for line in range(len(map)):
    for x in range(len(map[line])):
        if map[line][x]=="#":
            valid_positions.add((x,line))
            rocks.add((x,line))
        elif map[line][x]==".":
            valid_positions.add((x,line))

dirs=[0,1,2,3] #"R","D","L","U"

curr_pos=(8,0)
curr_dir=0
for instruction in instructions:
    if instruction=="R":
        curr_dir=(curr_dir+1)%4
        continue
    elif instruction=="L":
        curr_dir=(curr_dir-1)%4
        continue

    for _ in range(instruction):
        if curr_dir==0:
            new_pos=(curr_pos[0]+1,curr_pos[1])
            if new_pos not in valid_positions:
                new_pos=min(filter(lambda x: x[1]==new_pos[1],valid_positions),key=lambda x: x[0])
        elif curr_dir==1:
            new_pos=(curr_pos[0],curr_pos[1]+1)
            if new_pos not in valid_positions:
                new_pos=min(filter(lambda x: x[0]==new_pos[0],valid_positions),key=lambda x: x[1])
        elif curr_dir==2:
            new_pos=(curr_pos[0]-1,curr_pos[1])
            if new_pos not in valid_positions:
                new_pos=max(filter(lambda x: x[1]==new_pos[1],valid_positions),key=lambda x: x[0])
        elif curr_dir==3:
            new_pos=(curr_pos[0],curr_pos[1]-1)
            if new_pos not in valid_positions:
                new_pos=max(filter(lambda x: x[0]==new_pos[0],valid_positions),key=lambda x: x[1])

        if new_pos in rocks:
            break
        curr_pos=new_pos

print(curr_pos)
print((curr_pos[1]+1)*1000+(curr_pos[0]+1)*4+curr_dir)

# part 2
def find_new_pos_and_dir(curr_pos,curr_dir,new_pos):
    edges=[
    [(50,0),(99,0)],
    [(100,0),(149,0)],
    [(50,0),(50,49)],
    [(149,0),(149,49)],
    [(100,49),(149,49)],

    [(50,50),(50,99)],
    [(99,50),(99,99)],

    [(0,100),(49,100)],
    [(0,100),(0,149)],
    
    [(99,100),(99,149)],
    
    [(50,149),(99,149)],

    [(0,150),(0,199)],
    [(49,150),(49,199)],

    [(0,199),(49,199)],
    ]
    possible_edges=[idx for idx, edge in enumerate(edges) if (curr_pos[0]>=edge[0][0] and curr_pos[0]<=edge[1][0] and
           curr_pos[1]>=edge[0][1] and curr_pos[1]<=edge[1][1])]
    
    edge_transformation={
        (0,3): (11,0),
        (1,3):(13,3),
        (2,2):(8,0),
        (3,0):(9,2),
        (4,1):(6,2),
        (5,2):(7,1),
        (6,0):(4,3),
        (7,3):(5,0),
        (8,2):(2,0),
        (9,0):(3,2),
        (10,1):(12,2),
        (11,2):(0,1),
        (12,0):(10,3),
        (13,1):(1,1),
    }
    for edge in possible_edges:
        if (edge,curr_dir) in edge_transformation:
            new_edge_n,new_dir=edge_transformation[(edge,curr_dir)]
            curr_edge=edge
            break
    curr_edge=edges[curr_edge]
    if curr_edge[0][1]==curr_edge[1][1]:
        dist=curr_pos[0]-curr_edge[0][0]
    else:
        dist=curr_pos[1]-curr_edge[0][1]

    new_edge=edges[new_edge_n]
    if new_edge[0][1]==new_edge[1][1]:
        # 1, 0, 10, 7, 13, 4
        new_pos=(new_edge[0][0]+dist,new_edge[0][1])
    else:
        if new_edge_n in [3,9,2,8]:
            new_pos=(new_edge[0][0],new_edge[1][1]-dist)
        else: # 6, 12,11, 5
            new_pos=(new_edge[0][0],new_edge[0][1]+dist)
    return new_dir, new_pos

curr_pos=(50,0)
curr_dir=0

for instruction in instructions:
    if instruction=="R":
        curr_dir=(curr_dir+1)%4
        continue
    elif instruction=="L":
        curr_dir=(curr_dir-1)%4
        continue

    for _ in range(instruction):
        new_dir=curr_dir
        if curr_dir==0:
            new_pos=(curr_pos[0]+1,curr_pos[1])
        elif curr_dir==1:
            new_pos=(curr_pos[0],curr_pos[1]+1)
        elif curr_dir==2:
            new_pos=(curr_pos[0]-1,curr_pos[1])
        elif curr_dir==3:
            new_pos=(curr_pos[0],curr_pos[1]-1)
        if new_pos not in valid_positions:
            new_dir,new_pos=find_new_pos_and_dir(curr_pos,curr_dir,new_pos)
        if new_pos in rocks:
            break
        curr_pos=new_pos
        curr_dir=new_dir

print(curr_pos)
print((curr_pos[1]+1)*1000+(curr_pos[0]+1)*4+curr_dir)

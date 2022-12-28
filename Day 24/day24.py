f = open("Day 24\input.txt","r")
map=f.read().splitlines()

def get_blizzards(map):
    blizzards={}
    for line in range(len(map)):
        for x in range(len(map[0])):
            if map[line][x] in [">","^","<","v"]:
                blizzards[((x,line),map[line][x])]=None
    return blizzards

def get_possible_moves(loc,len_map,width_map,blizzards):
    options=[
        (loc[0],loc[1]),
        (loc[0]-1,loc[1]),
        (loc[0]+1,loc[1]),
        (loc[0],loc[1]-1),
        (loc[0],loc[1]+1),
    ]
    return [option for option in options if (option[0]>0 and 
            option[0]<=width_map and
            option[1]>0 and 
            option[1]<=len_map and 
            option not in blizzards)
            or option == (1,0) or option == (width_map,len_map+1)]

def find_new_locs_blizzards(blizzards):
    for blizzard in blizzards:
        if blizzard[1]==">":
            blizzards[blizzard]=(1+(blizzard[0][0])%width_map,blizzard[0][1])
        elif blizzard[1]=="<":
            blizzards[blizzard]=(1+(blizzard[0][0]-2)%width_map,blizzard[0][1])
        elif blizzard[1]=="^": 
            blizzards[blizzard]=((blizzard[0][0]),1+(blizzard[0][1]-2)%len_map)
        elif blizzard[1]=="v":
            blizzards[blizzard]=((blizzard[0][0]),1+(blizzard[0][1])%len_map)
    return blizzards

len_map=len(map)-2
width_map=len(map[0])-2
blizzards=get_blizzards(map)
current_positions={(1,0)}
time=0
at_exit=False
while not at_exit:
    #find new positions
    blizzards=find_new_locs_blizzards(blizzards)

    new_positions=set()
    for pos in current_positions:
        # find possible moves
        new_positions.update(get_possible_moves(pos,len_map,width_map,blizzards.values()))
    current_positions=new_positions
    blizzards={(blizzards[blizzard],blizzard[1]): None for blizzard in blizzards}
    at_exit=(width_map,len_map+1) in current_positions
    time+=1
    print(time)

# part 2
current_positions={(1,0)}
time=0
blizzards=get_blizzards(map)

at_exit=False
exit_reached=False
start_reached=False
while not (at_exit and exit_reached and start_reached):
    #find new positions
    blizzards=find_new_locs_blizzards(blizzards)

    new_positions=set()
    for pos in current_positions:
        # find possible moves
        new_positions.update(get_possible_moves(pos,len_map,width_map,blizzards.values()))
    current_positions=new_positions
    blizzards={(blizzards[blizzard],blizzard[1]): None for blizzard in blizzards}

    at_exit=(width_map,len_map+1) in current_positions
    if at_exit and not exit_reached:
        current_positions={(width_map,len_map+1)}
        exit_reached=True
        
    at_start=(1,0) in current_positions
    if exit_reached and at_start and not start_reached:
        current_positions={(1,0)}
        start_reached=True
        at_exit=False
    time+=1
    print(time)
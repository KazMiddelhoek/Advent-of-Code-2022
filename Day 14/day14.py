f = open("Day 14\input.txt","r")
rocks = f.read().splitlines()

rock_locs=set()
for rock in rocks:
    corners=rock.split(" -> ")
    for i in range(len(corners)-1):
        coords_start=[int(coord) for coord in corners[i].split(",")]
        coords_end=[int(coord) for coord in corners[i+1].split(",")]
        moving_in_y_direction = (coords_end[0]==coords_start[0])
        if  moving_in_y_direction:
            vertical_move_direction=1 if (coords_end[1]>coords_start[1]) else -1
            for k in range(coords_start[1],coords_end[1]+vertical_move_direction,vertical_move_direction):
                rock_locs.add((coords_start[0],k))
        else:
            horizontal_move_direction=1 if (coords_end[0]>coords_start[0]) else -1
            for k in range(coords_start[0],coords_end[0]+horizontal_move_direction,horizontal_move_direction):
                rock_locs.add((k,coords_start[1]))

occupied_locs=rock_locs.copy()
rock_below=True
n_sands_resting=0
while rock_below:
    sand_loc=[500,0]
    sand_not_resting=True

    while sand_not_resting and rock_below:
        rock_below=any(sand_loc[1]<rock[1] for rock in rock_locs)

        if (sand_loc[0], sand_loc[1]+1) not in occupied_locs:
            sand_loc[1]+=1
        elif (sand_loc[0]-1, sand_loc[1]+1) not in occupied_locs:
            sand_loc[1]+=1
            sand_loc[0]-=1
        elif (sand_loc[0]+1, sand_loc[1]+1) not in occupied_locs:
            sand_loc[1]+=1
            sand_loc[0]+=1
        else:
            occupied_locs.add(tuple(sand_loc))
            n_sands_resting+=1
            sand_not_resting=False
print(n_sands_resting)

#part 2
floor = max([rock[1] for rock in rock_locs])+2
occupied_locs=rock_locs
n_sands_resting=0
while (500,0) not in occupied_locs:
    sand_loc=[500,0]
    sand_not_resting=True
    while sand_not_resting:
        is_above_floor=(sand_loc[1]+1)<floor
        if (sand_loc[0], sand_loc[1]+1) not in occupied_locs and is_above_floor:
            sand_loc[1]+=1
        elif (sand_loc[0]-1, sand_loc[1]+1) not in occupied_locs and is_above_floor:
            sand_loc[1]+=1
            sand_loc[0]-=1
        elif (sand_loc[0]+1, sand_loc[1]+1) not in occupied_locs and is_above_floor:
            sand_loc[1]+=1
            sand_loc[0]+=1
        else:
            occupied_locs.add(tuple(sand_loc))
            n_sands_resting+=1
            sand_not_resting=False
print(n_sands_resting)

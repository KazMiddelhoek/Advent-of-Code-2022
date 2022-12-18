f = open("Day 18\input.txt","r")
cubes = f.read().splitlines()
cubes=[tuple([int(x) for x in cube.split(",")]) for cube in cubes]

def get_surrounding_locations(cube):
    return [
        (cube[0]-1,cube[1],cube[2]),
        (cube[0]+1,cube[1],cube[2]),
        (cube[0],cube[1]-1,cube[2]),
        (cube[0],cube[1]+1,cube[2]),
        (cube[0],cube[1],cube[2]-1),
        (cube[0],cube[1],cube[2]+1),
    ]


n_free_sides=0
for cube in cubes:
    locs=get_surrounding_locations(cube)
    for loc in locs:
        if loc not in cubes:
            n_free_sides+=1
print(n_free_sides)


#part 2
def can_reach_outside(loc,cubes,outside_locs):
    is_outside=False
    is_trapped=False
    visited={loc}
    current_locs={loc}
    while not is_outside and not is_trapped:
        new_current_locs=set()
        for loc in current_locs:
            surr=[sur_loc for sur_loc in get_surrounding_locations(loc) if sur_loc not in cubes and sur_loc not in visited]
            for sur_loc in surr:
                visited.add(sur_loc)
                new_current_locs.add(sur_loc)
        current_locs=new_current_locs
        is_outside=any(outside_loc in current_locs for outside_loc in outside_locs)
        is_trapped=not current_locs
    return is_outside, visited

n_free_sides=0
outside_locs=sorted(cubes)[0]
outside_locs=(outside_locs[0]-1,outside_locs[1],outside_locs[2])
outside_locs={outside_locs}
trapped_locs=set()
for cube in cubes:
    locs=get_surrounding_locations(cube)
    for loc in locs:
        if loc in cubes or loc in trapped_locs:
            continue
        if loc in outside_locs:
            n_free_sides+=1
            continue

        is_outside,visited=can_reach_outside(loc,cubes,outside_locs)
        if is_outside:
            n_free_sides+=1
            outside_locs.update(visited)        
        else:
            trapped_locs.update(visited)
print(n_free_sides)





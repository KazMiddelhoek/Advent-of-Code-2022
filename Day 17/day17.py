import math
f = open("Day 17\input.txt","r")
jet_pattern = f.readlines()[0]

rocks=[
    [[0,0],[1,0],[2,0],[3,0]],
    [[1,0],[0,1],[1,1],[2,1],[1,2]],
    [[0,0],[1,0],[2,0],[2,1],[2,2]],
    [[0,0],[0,1],[0,2],[0,3]],
    [[0,0],[1,0],[0,1],[1,1]],
]

rock_n=0
current_structure=set([(i,0) for i in range(7)])
initialize_rock=True
jet_n=0
height_loop=[]
while rock_n < 1671:
    jet=jet_pattern[jet_n%len(jet_pattern)]

    if initialize_rock:
        height_loop.append(max(current_structure,key=lambda x: x[1])[1])
        initialize_rock=False
        rock=rocks[rock_n%5]
        rock_pos=[2,max(current_structure,key=lambda x: x[1])[1]+4]
        rock=[[part[0]+rock_pos[0],part[1]+rock_pos[1] ] for part in rock]
    
    if jet ==">" and all(part[0]+1<7 and (part[0]+1,part[1]) not in current_structure for part in rock):
        rock=[[part[0]+1,part[1]] for part in rock]
    elif jet=="<" and all(part[0]-1>=0 and (part[0]-1,part[1]) not in current_structure for part in rock):
        rock=[[part[0]-1,part[1]] for part in rock]
    
    if all((part[0],part[1]-1) not in current_structure for part in rock):
        rock=[[part[0],part[1]-1] for part in rock]
    else:
        initialize_rock=True
        rock_n+=1
        current_structure.update([tuple(part) for part in rock])
    jet_n+=1
print(max(current_structure,key=lambda x: x[1])[1])
print(list(filter(lambda x: x[1]>2646, current_structure)))

#part 2
def find_new_contour(current_contour: set,rock):
    current_contour.update(rock)
    curr_pos=max(filter(lambda x: x[0]==0,current_contour),key=lambda x: x[1])
    new_contour={curr_pos}
    curr_direction="R"
    visited_end=False
    end_point = max(filter(lambda x: x[0]==6,current_contour),key=lambda x: x[1])
    while True:
        if end_point in new_contour:
            if (end_point[0]-1, end_point[1]) not in current_contour:
                break
            if (end_point[0]-1, end_point[1]) in new_contour and not visited_end:
                break
            if visited_end and curr_pos==end_point:
                break
            if not visited_end:
                curr_pos=(end_point[0]-1, end_point[1])
                new_contour.add(curr_pos)
                curr_direction="L"
                visited_end=True
            
        if curr_direction=="U":
            if (curr_pos[0]-1, curr_pos[1]) in current_contour:
                new_contour.add((curr_pos[0]-1, curr_pos[1]))
                curr_direction="L"
                curr_pos=(curr_pos[0]-1, curr_pos[1])
            elif (curr_pos[0], curr_pos[1]+1) in current_contour:
                new_contour.add((curr_pos[0], curr_pos[1]+1))
                curr_direction="U"
                curr_pos=(curr_pos[0], curr_pos[1]+1)
            elif (curr_pos[0]+1, curr_pos[1]) in current_contour:
                new_contour.add((curr_pos[0]+1, curr_pos[1]))
                curr_direction="R"
                curr_pos=(curr_pos[0]+1, curr_pos[1])
            elif (curr_pos[0], curr_pos[1]-1) in current_contour:
                new_contour.add((curr_pos[0], curr_pos[1]-1))
                curr_direction="D"
                curr_pos=(curr_pos[0], curr_pos[1]-1)

        elif curr_direction=="R":
            if (curr_pos[0], curr_pos[1]+1) in current_contour:
                new_contour.add((curr_pos[0], curr_pos[1]+1))
                curr_direction="U"
                curr_pos=(curr_pos[0], curr_pos[1]+1)
            elif (curr_pos[0]+1, curr_pos[1]) in current_contour:
                new_contour.add((curr_pos[0]+1, curr_pos[1]))
                curr_direction="R"
                curr_pos=(curr_pos[0]+1, curr_pos[1])
            elif (curr_pos[0], curr_pos[1]-1) in current_contour:
                new_contour.add((curr_pos[0], curr_pos[1]-1))
                curr_direction="D"
                curr_pos=(curr_pos[0], curr_pos[1]-1)
            elif (curr_pos[0]-1, curr_pos[1]) in current_contour:
                new_contour.add((curr_pos[0]-1, curr_pos[1]))
                curr_direction="L"
                curr_pos=(curr_pos[0]-1, curr_pos[1])

        elif curr_direction=="D":   
            if (curr_pos[0]+1, curr_pos[1]) in current_contour:
                new_contour.add((curr_pos[0]+1, curr_pos[1]))
                curr_direction="R"
                curr_pos=(curr_pos[0]+1, curr_pos[1])
            elif (curr_pos[0], curr_pos[1]-1) in current_contour:
                new_contour.add((curr_pos[0], curr_pos[1]-1))
                curr_direction="D"
                curr_pos=(curr_pos[0], curr_pos[1]-1)
            elif (curr_pos[0]-1, curr_pos[1]) in current_contour:
                new_contour.add((curr_pos[0]-1, curr_pos[1]))
                curr_direction="L"
                curr_pos=(curr_pos[0]-1, curr_pos[1])
            elif (curr_pos[0], curr_pos[1]+1) in current_contour:
                new_contour.add((curr_pos[0], curr_pos[1]+1))
                curr_direction="U"
                curr_pos=(curr_pos[0], curr_pos[1]+1)

        elif curr_direction=="L":   
            if (curr_pos[0], curr_pos[1]-1) in current_contour:
                new_contour.add((curr_pos[0], curr_pos[1]-1))
                curr_direction="D"
                curr_pos= (curr_pos[0], curr_pos[1]-1)
            elif (curr_pos[0]-1, curr_pos[1]) in current_contour:
                new_contour.add((curr_pos[0]-1, curr_pos[1]))
                curr_direction="L"
                curr_pos=(curr_pos[0]-1, curr_pos[1])
            elif (curr_pos[0], curr_pos[1]+1) in current_contour:
                new_contour.add((curr_pos[0], curr_pos[1]+1))
                curr_direction="U"
                curr_pos=(curr_pos[0], curr_pos[1]+1) 
            elif (curr_pos[0]+1, curr_pos[1]) in current_contour:
                new_contour.add((curr_pos[0]+1, curr_pos[1]))
                curr_direction="R"
                curr_pos= (curr_pos[0]+1, curr_pos[1])

    new_height=min(new_contour,key=lambda x: x[1])[1]
    new_contour=set([(pos[0],pos[1]-new_height) for pos in new_contour])
    return new_contour,new_height

rock_n=0
current_contour=set([(i,0) for i in range(7)])
current_rock=[]
initialize_rock=True
jet_n=0
len_jet=len(jet_pattern)
states={}
current_height=0
max_rock_n=1_000_000_000_000
while rock_n < max_rock_n:
    jet=jet_pattern[jet_n%len_jet]

    if initialize_rock:
        initialize_rock=False
        rock=rocks[rock_n%5]
        rock_pos=[2,max(current_contour,key=lambda x: x[1])[1]+4]
        rock=[[part[0]+rock_pos[0],part[1]+rock_pos[1] ] for part in rock]

        if states.get((jet_n%len_jet,rock_n%5,tuple(current_contour)),None) is not None:
            last_height,last_rock_n,last_jet_n=states[(jet_n%len_jet,rock_n%5,tuple(current_contour))]
            height_increase=current_height-last_height
            rock_increase=rock_n-last_rock_n
            jet_increase=jet_n-last_jet_n
            multiplier=math.floor((max_rock_n-rock_n)/rock_increase)
            current_height+=multiplier*height_increase
            rock_n+=multiplier*rock_increase
            jet_n+=multiplier*jet_increase
        else:
            states[(jet_n%len_jet,rock_n%5,tuple(current_contour))]=(current_height, rock_n, jet_n)
 
    # move sideways
    if jet ==">" and all(part[0]+1<7 and (part[0]+1,part[1]) not in current_contour for part in rock):
        rock=[[part[0]+1,part[1]] for part in rock]
    elif jet=="<" and all(part[0]-1>=0 and (part[0]-1,part[1]) not in current_contour for part in rock):
        rock=[[part[0]-1,part[1]] for part in rock]

    #Move down
    if all((part[0],part[1]-1) not in current_contour for part in rock):
        rock=[[part[0],part[1]-1] for part in rock]
    else:
        initialize_rock=True
        rock_n+=1
        current_contour,new_height=find_new_contour(current_contour,[tuple(part) for part in rock]) 
        current_height+=new_height             
    jet_n+=1
print(current_height)
print(current_height+max(current_contour,key=lambda x: x[1])[1])
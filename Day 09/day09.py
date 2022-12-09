f = open("Day 09\input.txt","r")
movements = f.read().splitlines()
movements=[movement.split(" ") for movement in movements]

def find_visited_locations(body_parts):
    visited_locations=set((tuple(body_parts[-1]),))
    for movement in movements:
        for _ in range(int(movement[1])):
            if movement[0]=="U":
                body_parts[0][1]=body_parts[0][1]+1        
            elif movement[0]=="R":
                body_parts[0][0]=body_parts[0][0]+1
            elif movement[0]=="D":
                body_parts[0][1]=body_parts[0][1]-1
            elif movement[0]=="L":
                body_parts[0][0]=body_parts[0][0]-1
            
            for i, _ in enumerate(body_parts[1:],start=1):
                diff=[abs(body_parts[i-1][0]-body_parts[i][0]),abs(body_parts[i-1][1]-body_parts[i][1])]
                if any(dist>1 for dist in diff):
                    tail_movement=[int((first_part-second_part)/max(1,abs(first_part-second_part))) for first_part,second_part in zip(body_parts[i-1],body_parts[i])]
                    body_parts[i]=[sum(x) for x in zip(body_parts[i],tail_movement)]
            visited_locations.add(tuple(body_parts[-1]))
    return visited_locations

#part 1
body_parts=[[0,0] for _ in range(2)]
print(len(find_visited_locations(body_parts)))

#part 2
body_parts=[[0,0] for _ in range(10)]
print(len(find_visited_locations(body_parts)))
f = open("Day 12\input.txt","r")
map = f.read().splitlines()

start=(0,20)
end=False
current_points=[start]
visited=set((start,))

def get_surrounding_points(point):
    surr_points=[
        (point[0],point[1]+1),
        (point[0]+1,point[1]),
        (point[0],point[1]-1),
        (point[0]-1,point[1]),
    ]
    return [point for point in surr_points if not any(coord<0 for coord in point) and point[1]<len(map) and point[0]<len(map[0])]

steps=0
while not end:
    new_current_points=[]
    for point in current_points:
        surr_points=get_surrounding_points(point)
        for sur_point in surr_points:
            if ((sur_point not in visited and ord(map[sur_point[1]][sur_point[0]]) <= (ord(map[point[1]][point[0]])+1) and map[sur_point[1]][sur_point[0]]!="E") or 
                (map[point[1]][point[0]]=="S") or 
                ((map[sur_point[1]][sur_point[0]]=="E") and ord(map[point[1]][point[0]])>=121)):
                visited.add(sur_point)
                new_current_points.append(sur_point)
                if map[sur_point[1]][sur_point[0]]=="E":
                    end=True
                    break
    current_points=new_current_points
    steps+=1
print(steps)

# part 2
start=(58,20)
end=False
current_points=[start]
visited=set((start,))

steps=0
while not end:
    new_current_points=[]
    for point in current_points:
        surr_points=get_surrounding_points(point)
        for sur_point in surr_points:
            if ((sur_point not in visited and 
            ord(map[sur_point[1]][sur_point[0]]) >= (ord(map[point[1]][point[0]])-1) and (map[point[1]][point[0]]!="E")) or 
                (map[point[1]][point[0]]=="S") or 
                ((map[point[1]][point[0]]=="E") and ord(map[sur_point[1]][sur_point[0]])>=121)):
                visited.add(sur_point)
                new_current_points.append(sur_point)
                if map[sur_point[1]][sur_point[0]]=="a":
                    end=True
                    break
    current_points=new_current_points
    steps+=1
print(steps)
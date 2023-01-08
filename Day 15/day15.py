f = open("Day 15\input.txt","r")
sensor_readings = f.read().splitlines()

sensors=[]
beacons=[]
for sensor_reading in sensor_readings:
    sensor_reading=sensor_reading.split(":")
    sensor_pos=sensor_reading[0].split(", y=")
    sensor_pos=(int(sensor_pos[0].split("x=")[1]),int(sensor_pos[1]))
    sensors.append(sensor_pos)
    beacon_pos=sensor_reading[1].split(", y=")
    beacon_pos=(int(beacon_pos[0].split("x=")[1]),int(beacon_pos[1]))
    beacons.append(beacon_pos)

def calc_manhattan_dist(sensor,beacon):
    return sum([abs(sensor[0]-beacon[0]), abs(sensor[1]-beacon[1])])
# part 1
scanned_in_row=set()
y=2_000_000
for sensor, beacon in zip(sensors,beacons):
    dist=calc_manhattan_dist(sensor,beacon)
    if ((sensor[1] >= y) and (sensor[1]-dist)<= y) or (sensor[1] <= y and (sensor[1]+dist) >=y):
        width=abs(dist-abs(sensor[1]-y))
        for i in range(-width, width+1):
            scanned_in_row.add((sensor[0]+i,y))
            
min_scanned=min([scanned[0] for scanned in scanned_in_row])
max_scanned=max([scanned[0] for scanned in scanned_in_row])
n_scanned_spots=0
for i in range(min_scanned,max_scanned+1):
    if (i,y) in scanned_in_row and (i,y) not in sensors and (i,y) not in beacons:
        n_scanned_spots+=1
print(n_scanned_spots)

# part 2
sensor_dists=[]
for sensor, beacon in zip(sensors,beacons):
    dist=calc_manhattan_dist(sensor,beacon)
    sensor_dists.append(dist)

found=False
for y in range(0,4_000_001):
    scanned_ranges=[]
    for sensor,sensor_dist in zip(sensors,sensor_dists):
        if ((sensor[1] >= y) and (sensor[1]-sensor_dist)<= y) or (sensor[1] <= y and (sensor[1]+sensor_dist) >=y):
            width=abs(sensor_dist-abs(sensor[1]-y))
            scanned_ranges.append([max(0,sensor[0]-width),min(4_000_000,sensor[0]+width)])
    
    scanned_ranges=sorted(scanned_ranges)

    # merge ranges
    total_range=scanned_ranges[0]
    for i in range(1,len(scanned_ranges)):
        if scanned_ranges[i][0]<=(total_range[1]+1):
            total_range[1]=max(scanned_ranges[i][1],total_range[1])
        else:
            found=True
            x=total_range[1]+1
            break
    if found:
        break

print(x*4_000_000+y)
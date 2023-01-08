f = open("Day 16\input.txt","r")
valve_strs = f.read().splitlines()

valves={}
for valve in valve_strs:
    valve=(valve.replace("Valve ","").replace(" has flow rate="," ").replace("; tunnels lead to valves "," ")
                .replace("; tunnel leads to valve "," ").replace(", ","-").split(" "))
    valves[valve[0]]={"flow_rate": int(valve[1]),
                        "connected_to": valve[2].split("-"),
                        "is_open": False,
                        "expected_return": 0
                    }

def calc_travel_time(current_location,to_valve,valves):
    connected_valves={current_location}
    travel_time=0
    while to_valve not in connected_valves:
        for valve in connected_valves.copy():
            for conn_valve in valves[valve]["connected_to"]:
                connected_valves.add(conn_valve)
        travel_time+=1
    return travel_time

def calc_travel_times(flow_valves):
    travel_times={}
    for i,key in enumerate(flow_valves):
        for j,key2 in enumerate(flow_valves):
            if j>i:
                travel_times[(key,key2)]=calc_travel_time(key,key2,valves)
                travel_times[(key2,key)]=calc_travel_time(key,key2,valves)
    return travel_times

def find_max_pressure(current_time,current_pos,curr_pressure,flow_valves):
    flow_valves[current_pos]["is_open"]=True
    visited.append(current_pos)
    outcomes["-".join(visited)]=curr_pressure

    if not any(travel_times[travel_time] < 31-current_time for travel_time in travel_times if current_pos in travel_time[0] and not flow_valves[travel_time[1]]["is_open"]):
        visited.pop()
        flow_valves[current_pos]["is_open"]=False
        return
        
    pos_temp=current_pos
    for valve in flow_valves:
        if not flow_valves[valve]["is_open"] and valve!=current_pos and travel_times[(current_pos,valve)] < 31-current_time:
            find_max_pressure(
                current_time+travel_times[(current_pos,valve)]+1,
                valve,
                curr_pressure+(30-(current_time+travel_times[(current_pos,valve)]+1))*flow_valves[valve]["flow_rate"],
                flow_valves)
    visited.pop()
    flow_valves[current_pos]["is_open"]=False


flow_valves={k: v for k,v in valves.items() if v["flow_rate"]!=0 or k=="AA"}
flow_valves["AA"]["is_open"]=True
travel_times=calc_travel_times(flow_valves)

current_location="AA"
current_time=0
curr_pressure=0
outcomes={}
visited=[]
find_max_pressure(0,"AA",curr_pressure,flow_valves)
max_pressure=max(outcomes,key= lambda x: outcomes[x])
print(max_pressure)
print(outcomes[max_pressure])

# part 2
def find_max_pressure_with_elephant(
    time_you,
    time_elephant,
    pos_you,pos_elephant,
    curr_pressure,
    flow_valves,
    moved,current_max):
    flow_valves[pos_you]["is_open"]=True
    flow_valves[pos_elephant]["is_open"]=True
    if moved=="you":
        visited.append("Y-"+str(time_you)+"-"+pos_you)
    else:
        visited.append("E-"+str(time_elephant)+"-"+pos_elephant)
    print(visited)
    outcomes["-".join(visited)]=curr_pressure
        

    you_cant_move=not any(travel_times[valve_combi] < 27-time_you for valve_combi in travel_times if pos_you in valve_combi[0] and not flow_valves[valve_combi[1]]["is_open"])
    elephant_cant_move=not any(travel_times[valve_combi] < 27-time_elephant for valve_combi in travel_times if pos_elephant in valve_combi[0] and not flow_valves[valve_combi[1]]["is_open"])
    
    time_left=(26-(min(time_you,time_elephant) +1))
    time_range= [i for i in range(time_left,0,-1) for _ in range(2)]
    closed_valves={key: val for key, val in flow_valves.items() if not flow_valves[key]["is_open"]}

    current_max=max(current_max,curr_pressure)
    max_achievable_pressure=curr_pressure+ sum([time*flow_valves[valve]["flow_rate"] for time,valve in zip(time_range,closed_valves)])
    cant_improve_current_best=max_achievable_pressure<current_max

    if (you_cant_move and elephant_cant_move) or cant_improve_current_best:
        visited.pop()
        if moved=="you":
            flow_valves[pos_you]["is_open"]=False
        else:
            flow_valves[pos_elephant]["is_open"]=False
        return current_max

    if (time_elephant<=time_you) or you_cant_move:
        for valve in flow_valves:
            if not flow_valves[valve]["is_open"] and (valve!=pos_elephant) and (travel_times[(pos_elephant,valve)] < 27-time_elephant):
                current_max=find_max_pressure_with_elephant(
                    time_you,
                    time_elephant+travel_times[(pos_elephant,valve)]+1,
                    pos_you,
                    valve,
                    curr_pressure+(26-(time_elephant+travel_times[(pos_elephant,valve)]+1))*flow_valves[valve]["flow_rate"],
                    flow_valves,
                    "elephant",current_max)
    elif (time_you<time_elephant) or elephant_cant_move:
        for valve in flow_valves:
            if not flow_valves[valve]["is_open"] and valve!=pos_you and travel_times[(pos_you,valve)] < 27-time_you:
                current_max=find_max_pressure_with_elephant(
                    time_you+travel_times[(pos_you,valve)]+1,
                    time_elephant,
                    valve,
                    pos_elephant,
                    curr_pressure+(26-(time_you+travel_times[(pos_you,valve)]+1))*flow_valves[valve]["flow_rate"],
                    flow_valves,
                    "you",current_max)
    visited.pop()
    if moved=="you":
        flow_valves[pos_you]["is_open"]=False
    else:
        flow_valves[pos_elephant]["is_open"]=False
    return current_max

flow_valves={k: v for k,v in valves.items() if v["flow_rate"]!=0 or k=="AA"}
flow_valves["AA"]["is_open"]=True
flow_valves={key: val for key, val in sorted(flow_valves.items(), key = lambda ele: ele[1]["flow_rate"], reverse = True)}
travel_times=calc_travel_times(flow_valves)

pos_you="AA"
pos_elephant="AA"
time_you=0
time_elephant=0
curr_pressure=0
current_max=0
outcomes={}
visited=[]
current_max=find_max_pressure_with_elephant(time_you,time_elephant,pos_you,pos_elephant,curr_pressure,flow_valves,"elephant",current_max)
max_pressure=max(outcomes,key= lambda x: outcomes[x])
print(max_pressure)
print(outcomes[max_pressure])
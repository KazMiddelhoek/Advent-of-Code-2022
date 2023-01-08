import re
f = open("Day 19\input.txt","r")
blueprint_text=f.read().splitlines()

blueprints={}
robots=["ore_robot","clay_robot","obsidian_robot","geodes_robot"]
for i,blueprint in enumerate(blueprint_text,1):
    robot_costs=blueprint.replace(":",".").split(".")
    blueprints[i]={
        robots[3]:{"ore": int(re.findall(r'\d+',robot_costs[4])[0]),
              "obsidian": int(re.findall(r'\d+',robot_costs[4])[1])},
        robots[2]:{"ore": int(re.findall(r'\d+',robot_costs[3])[0]),
                  "clay": int(re.findall(r'\d+',robot_costs[3])[1])},
        robots[1]:{"ore": int(re.findall(r'\d+',robot_costs[2])[0])},
        robots[0]:{"ore": int(re.findall(r'\d+',robot_costs[1])[0])},
    }

def get_options(resources,blueprint,forbidden_bots,current_robots: list,robot_limits):
    options=[]
    for robot in blueprints[blueprint]:
        if (all(resources[cost] >= blueprints[blueprint][robot][cost] for cost in blueprints[blueprint][robot]) and 
                robot not in forbidden_bots and
                (robot=="geodes_robot" or current_robots.count(robot)<robot_limits[robot])):
            options.append(robot)
    
    if "geodes_robot" in options:
        options.append(None)
    elif "obsidian_robot" in current_robots and "geodes_robot" not in options:
        options.insert(0,None)
    elif "clay_robot" in current_robots and "obsidian_robot" not in options:
        options.insert(0,None)
    else:
        options.append(None)
    
    return options

def  calc_max_robots(blueprint):
    max_robots={"ore_robot": 0,
    "clay_robot":0,
    "obsidian_robot":0,
    }
    for robot in blueprint:
        for resource in ["ore","clay","obsidian"]:
            max_robots[resource+"_robot"]=max(max_robots[resource+"_robot"],blueprint[robot].get(resource,0))
    return max_robots

def cant_exceed_max_geodes(minute,current_robots,resources,current_max,max_time):
    return current_max>(len(list(filter(lambda robot: robot=="geodes_robot",current_robots)))*(max_time+1-minute)
    +sum(range(max_time-minute,0,-1))+resources["geodes"]
    )

def find_max_geodes(blueprint,resources: dict,current_robots:list,minute,max_geodes: dict,forbidden_bots,robot_limits,max_time):
    minute+=1
    if cant_exceed_max_geodes(minute,current_robots,resources,max_geodes.get(blueprint,0),max_time):
        return
    if minute>max_time:
        return

    options=get_options(resources,blueprint,forbidden_bots,current_robots,robot_limits)

    for robot in current_robots:
        resources[robot.replace("_robot","")]+=1
    max_geodes[blueprint]=max(max_geodes.get(blueprint,0),resources["geodes"])
    
    for option in options:
        resources_temp=resources.copy()
        robots_temp=current_robots.copy()
        if option is not None: #buy robot
            robots_temp.append(option)
            for resource in blueprints[blueprint][option]:
                resources_temp[resource]-=blueprints[blueprint][option][resource]
            forbidden_bots=[]
        else:
            if not forbidden_bots:
                forbidden_bots=list(filter(lambda x: x is not None,options))
        find_max_geodes(blueprint,resources_temp,robots_temp,minute,max_geodes,forbidden_bots,robot_limits,max_time)
        
max_geodes={}
max_time=24
for blueprint in blueprints:
    resources={
        "ore":0,
        "clay":0,
        "obsidian":0,
        "geodes":0
    }
    current_robots=["ore_robot"]
    minute=0
    robot_limits=calc_max_robots(blueprints[blueprint])
    find_max_geodes(blueprint,resources,current_robots,minute,max_geodes,[],robot_limits,max_time)

print(max_geodes)
print(sum([key*val for key, val in max_geodes.items()]))

#part 2
max_geodes={}
max_time=32
blueprints={k: v for k,v in blueprints.items() if k in [1,2,3]}
for blueprint in blueprints:
    resources={
    "ore":0,
    "clay":0,
    "obsidian":0,
    "geodes":0
    }
    current_robots=["ore_robot"]
    minute=0
    robot_limits=calc_max_robots(blueprints[blueprint])
    find_max_geodes(blueprint,resources,current_robots,minute,max_geodes,[],robot_limits,max_time)
    print(max_geodes)

print(max_geodes)
ans=1
for val in max_geodes.values():
    ans*=val
print(ans)
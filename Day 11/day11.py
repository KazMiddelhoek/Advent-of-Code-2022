f = open("Day 11\input.txt","r")
lines = f.read().splitlines()

def prepare_monkeys(lines):
    monkeys=[]
    for line in lines:
        if line=="":
            continue
        if line[0]=="M":
            monkeys.append({"items inspected": 0})
        elif line[2]=="S":
            monkeys[-1]["items"]=[int(item) for item in line[17:].split(", ")]
        elif line[2]=="O":
            monkeys[-1]["operation"]=[line[23],line.split(" ")[-1]]
        elif line[2]=="T":
            monkeys[-1]["test"]=int(line.split(" ")[-1])
        elif line[4:11]=="If true":
            monkeys[-1]["to"]=[int(line.split(" ")[-1])]
        elif line[4:12]=="If false":
             monkeys[-1]["to"].append(int(line.split(" ")[-1]))
    return monkeys

def operate_on_item(monkey,i):
    if monkey["operation"][0]=="*" and monkey["operation"][1]=="old":
        monkey["items"][i]=monkey["items"][i]**2
    elif monkey["operation"][0]=="*":
        monkey["items"][i]*=int(monkey["operation"][1])
    elif monkey["operation"][0]=="+":
        monkey["items"][i]+=int(monkey["operation"][1])

def pass_item(monkey,i,monkeys):
    if (monkey["items"][i]%monkey["test"])==0:
        monkeys[monkey["to"][0]]["items"].append(monkey["items"][i])       
    else:
        monkeys[monkey["to"][1]]["items"].append(monkey["items"][i])    

# part 1
monkeys=prepare_monkeys(lines)
for round in range(20):
    for monkey in monkeys:
        monkey["items inspected"]+=len(monkey["items"])
        for i, _ in enumerate(monkey["items"]):
            operate_on_item(monkey,i)
            monkey["items"][i]=monkey["items"][i]//3
            pass_item(monkey,i,monkeys)

        monkey["items"]=[]

monkey_inspections=sorted([monkey["items inspected"] for monkey in monkeys],reverse=True)
print(monkey_inspections[0]*monkey_inspections[1])

# part 2
monkeys=prepare_monkeys(lines)

divisor=monkeys[0]["test"]
for monkey in monkeys[1:]:
    divisor*=monkey["test"]

for round in range(10_000):
    for k,monkey in enumerate(monkeys):
        monkey["items inspected"]+=len(monkey["items"])
        for i, _ in enumerate(monkey["items"]):
            operate_on_item(monkey,i)   
            monkey["items"][i]=monkey["items"][i]%divisor
            pass_item(monkey,i,monkeys)
        monkey["items"]=[]

monkey_inspections=sorted([monkey["items inspected"] for monkey in monkeys],reverse=True)
print(monkey_inspections[0]*monkey_inspections[1])


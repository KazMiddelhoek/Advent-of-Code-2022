f = open("Day 10\input.txt","r")
instructions = f.read().splitlines()

signal_strengths=[]
cycle=1
X=1
for instruction in instructions:
    if instruction=="noop":
        if (cycle-20)%40==0 or cycle==20:
            signal_strengths.append(cycle*X)
        cycle+=1
    else:
        for i in range(2):
            if (cycle-20)%40==0 or cycle==20:
                signal_strengths.append(cycle*X)
            cycle+=1
        X+=int(instruction.split(" ")[1])
    if cycle>=220:
        break
print(sum(signal_strengths))

#part 2
def draw_pixel(cycle,X):
    if (cycle-1)%40==0:
        print("")
    if abs((cycle-1)%40 - X) <=1:
        print("#",end="")
    else:
        print(".",end="")

cycle=1
X=1
for instruction in instructions:
    if instruction=="noop":
        draw_pixel(cycle,X)
        cycle+=1
    else:
        for i in range(2):
            draw_pixel(cycle,X)
            cycle+=1
        X+=int(instruction.split(" ")[1])
print(sum(signal_strengths))
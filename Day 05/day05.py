f = open("Day 05\input.txt","r")
lines = f.read().splitlines()

def create_stacks(lines):
    n_stacks=9
    stacks=[[] for _ in range(n_stacks)]
    for i in range(7,-1,-1):
        for stack in range(9):
            if lines[i][1+stack*4]!=" ":
                stacks[stack].append(lines[i][1+stack*4])
    return stacks

stacks=create_stacks(lines)

for move in lines[10:]:
    move=move[5:]
    for word in [" from "," to "]:
        move=move.replace(word,"-")
    n,from_stack,to_stack=[int(n) for n in move.split("-")]
    from_stack,to_stack=from_stack-1,to_stack-1

    stacks[to_stack].extend(reversed(stacks[from_stack][-n:]))
    stacks[from_stack]=stacks[from_stack][:-n]

[print(stack[-1],end="") for stack in stacks]

#part 2
stacks=create_stacks(lines)
for move in lines[10:]:
    move=move[5:]
    for word in [" from "," to "]:
        move=move.replace(word,"-")
    n,from_stack,to_stack=[int(n) for n in move.split("-")]
    from_stack,to_stack=from_stack-1,to_stack-1

    stacks[to_stack].extend(stacks[from_stack][-n:])
    stacks[from_stack]=stacks[from_stack][:-n]
    
print("\n")
[print(stack[-1],end="") for stack in stacks]



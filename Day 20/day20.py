f = open("Day 20\input.txt","r")
import math
instructions = [int(instruction) for instruction in f.read().splitlines()]

ids={"id_"+str(i):instruction for i,instruction in enumerate(instructions)}
id_list=["id_"+str(i) for i, _ in enumerate(instructions)]

n_ids=len(id_list)
reordering_ids=id_list.copy()
for instruction in id_list:
    curr_idx=reordering_ids.index(instruction)
    new_idx=(curr_idx+ids[instruction])
    if new_idx<=0:        
        new_idx=(new_idx-1-abs(math.ceil(new_idx/n_ids)))%n_ids
    elif new_idx>n_ids:
        new_idx=(new_idx+(math.floor(new_idx/n_ids)))%n_ids
    reordering_ids.remove(instruction)
    reordering_ids=reordering_ids[:new_idx]+[instruction] +reordering_ids[new_idx:]
final_list=[ids[id_] for id_ in reordering_ids]
zero_loc=final_list.index(0)
print(final_list[(zero_loc+1000)%n_ids]+final_list[(zero_loc+2000)%n_ids]+final_list[(zero_loc+3000)%n_ids])

# part 2
instructions=[instruction * 811_589_153 for instruction in instructions]
ids={"id_"+str(i):instruction for i,instruction in enumerate(instructions)}
id_list=["id_"+str(i) for i, _ in enumerate(instructions)]

n_ids=len(id_list)
reordering_ids=id_list.copy()

for _ in range(10):
    for instruction in id_list:
        steps=ids[instruction]
        if steps==0:
            continue
        curr_idx=reordering_ids.index(instruction)
        new_idx=curr_idx+steps
        if new_idx==0:
            new_idx=n_ids-1
        elif new_idx<0:        
            new_idx=(n_ids-1)-abs(new_idx)%(n_ids-1)
        elif new_idx>n_ids:
            new_idx=1+(new_idx-1)%(n_ids-1)
        reordering_ids.remove(instruction)
        reordering_ids=reordering_ids[:new_idx]+[instruction]+reordering_ids[new_idx:]
        
final_list=[ids[id_] for id_ in reordering_ids]
zero_loc=final_list.index(0)

print(final_list[(zero_loc+1000)%n_ids]+final_list[(zero_loc+2000)%n_ids]+final_list[(zero_loc+3000)%n_ids])

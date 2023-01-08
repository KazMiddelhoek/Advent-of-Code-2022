from functools import cmp_to_key

f = open("Day 13\input.txt","r")
packets = f.read().splitlines()
packets=[eval(packet) if packet != "" else "" for packet in packets]
pairs=[[],]
for packet in packets:
    if packet=="":
        pairs.append([])
    else:
        pairs[-1].append(packet)

def compare_pairs(left,right):
    if isinstance(left,int) and isinstance(right,int):
        if left==right:
            return None
        else:
            return left<right

    left,right = [[val] if isinstance(val,int) else val for val in [left,right]]
    for left_elem, right_elem in zip(left,right):
        is_right_order=compare_pairs(left_elem,right_elem)
        if is_right_order is None:
            continue
        return is_right_order
    if len(left)==len(right):
        return None
    else:
        return len(left)<len(right)

right_order=[]
i=1
for left,right in pairs:
    is_right_order=compare_pairs(left,right)
    if is_right_order:
         right_order.append(i)
    i+=1
print(sum(right_order))

# part 2
def compare_wrapper(left,right):
    is_right_order=compare_pairs(left,right)
    if is_right_order:
        return -1
    else:
        return 1

f = open("Day 13\input.txt","r")
packets = f.read().splitlines()
packets=[eval(packet) for packet in packets if packet != "" ]
packets=packets+[[[2]],[[6]]]
packets=sorted(packets,key=cmp_to_key(compare_wrapper),)
print((packets.index([[2]])+1) *(packets.index([[6]])+1))

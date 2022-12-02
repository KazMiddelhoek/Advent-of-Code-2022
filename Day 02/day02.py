f = open("Day 02\input.txt","r")
lines = f.read().splitlines()

def winning_score(opp,you):
    if (opp==1) and (you==3):
        return 0
    elif (opp==3) and (you==1):
        return 6
    elif opp==you:
        return 3
    elif you>opp:
        return 6
    else:
        return 0

scores={
    "A":1,
    "B":2,
    "C":3,
    "X": 1,
    "Y": 2,
    "Z": 3}

total_score=0
for line in lines:
    score=scores[line[-1]]+winning_score(scores[line[0]], scores[line[-1]])
    print(score)
    total_score+=score
print(total_score)


# part 2
def find_hand(opp,you):
    if (you=="X") and (opp == 1):
        return 3
    elif you=="X":
        return opp-1
    elif you=="Y":
        return opp
    else:
        return (opp)%3 + 1

f = open("Day 02\input.txt","r")
lines = f.read().splitlines()

total_score=0
for line in lines:
    picked_option=find_hand(scores[line[0]], line[-1])
    score=picked_option+winning_score(scores[line[0]], picked_option)
    total_score+=score
print(total_score)

f = open("Day 08\input.txt","r")
forest = f.read().splitlines()

def is_visible(y,x,forest):
    return (
        all(tree <forest[y][x] for tree in forest[y][:x]) or 
        all(tree<forest[y][x] for tree in forest[y][(x+1):]) or
        all(tree <forest[y][x] for tree in [row[x] for row in forest[:y]]) or
        all(tree <forest[y][x] for tree in [row[x] for row in forest[(y+1):]]) )

n_visible_trees=2*len(forest)+2*len(forest[0])-4
for y in range(1,len(forest)-1):
    for x in range(1,len(forest[0])-1):
        if is_visible(y,x,forest):
            n_visible_trees+=1
print(n_visible_trees)

#part 2
def find_score_from_view(view):
    score=view.find("1")+1
    if score==0:
        score=len(view)
    return score

highest_viewing_score=0
for y in range(1,len(forest)-1):
    for x in range(1,len(forest[0])-1):
        view_left="".join([str(int(tree>=forest[y][x])) for tree in forest[y][(x-1)::-1]])
        view_right="".join([str(int(tree>=forest[y][x])) for tree in forest[y][(x+1):]])
        view_above="".join([str(int(tree>=forest[y][x])) for tree in "".join([row[x] for row in forest[:y]])[::-1]])
        view_under="".join([str(int(tree>=forest[y][x])) for tree in "".join([row[x] for row in forest[(y+1):]])])

        scores=[find_score_from_view(view) for view in [view_left,view_right,view_above,view_under]]
        current_score=1
        for score in scores:
            current_score*=score

        if current_score>highest_viewing_score:
            highest_viewing_score=current_score
print(highest_viewing_score)
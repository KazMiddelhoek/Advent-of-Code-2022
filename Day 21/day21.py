f = open("Day 21\input.txt","r")
shoutings =  {shouting.split(": ")[0]: shouting.split(": ")[1] for shouting in f.read().splitlines()}

def get_known_unknown(shoutings):
    known_numbers={}
    unknown={}
    for shouting in shoutings:
        try:
            known_numbers[shouting]=int(shoutings[shouting])
        except:
            unknown[shouting]=shoutings[shouting]
    return unknown,known_numbers

unknown,known_numbers=get_known_unknown(shoutings)

while unknown:
    for person in unknown.copy():
        for operator in [" + "," - "," / "," * "]:
            needed=unknown[person].split(operator)
            if len(needed)==1:
                continue
            one=known_numbers.get(needed[0],None)
            two=known_numbers.get(needed[1],None)
            if one is None or two is None:
                continue

            if operator==" + ":
                known_numbers[person]=int(one)+int(two)
            elif operator==" - ":
                known_numbers[person]=int(one)-int(two)
            elif operator==" / ":
                known_numbers[person]=int(one)/int(two)
            elif operator==" * ":
                known_numbers[person]=int(one)*int(two)
            unknown.pop(person)
            break     
print(known_numbers["root"])

#part 2
unknown,known_numbers=get_known_unknown(shoutings)

unknown["root"]=unknown["root"].split(" + ")[0] + " == " + unknown["root"].split(" + ")[1]
known_numbers["humn"]="X"
updated=True
while updated:
    updated=False
    for person in unknown.copy():
        for operator in [" + "," - "," / "," * "]:
            needed=unknown[person].split(operator)
            if len(needed)==1:
                continue
            one=known_numbers.get(needed[0],None)
            two=known_numbers.get(needed[1],None)
            if one is None or two is None or one=="X" or two=="X":
                continue

            if operator==" + ":
                known_numbers[person]=int(one)+int(two)
            elif operator==" - ":
                known_numbers[person]=int(one)-int(two)
            elif operator==" / ":
                known_numbers[person]=int(one)/int(two)
            elif operator==" * ":
                known_numbers[person]=int(one)*int(two)
            unknown.pop(person)
            updated=True
            break 

current_eq=["root"]
updated=True
while updated:
    updated=False
    new_eq=[]
    for i in range(len(current_eq)):
        if current_eq[i] not in ["+","-","/","*","==","(",")"] and not isinstance(current_eq[i],int):
            number=known_numbers.get(current_eq[i],None)
            if number is not None:
                new_eq.append(str(number))
                updated=True
            else:
                var=unknown.get(current_eq[i],None)
                if var is not None:
                    new_eq.append("( "+var+" )")
                    updated=True
                else:
                    new_eq.append(current_eq[i])
        else:
            new_eq.append(current_eq[i])
    new_eq=[x for var in new_eq for x in var.split(" ")]
    current_eq=new_eq

# simplify string equation
import sympy
current_eq="".join(current_eq)
current_eq=current_eq.replace("==","=")
X=sympy.Symbol("X")
print(sympy.solve(eval(current_eq.split("=")[0][1:])-eval(current_eq.split("=")[1][:-1]),dict=True))
with open("8.txt") as f:
    lines = f.read().splitlines()
instructions= [(line[:3],int(line[4:])) for line in lines]
visited=set()
accCount=0
instrucPointer=0
while not instrucPointer in visited:
    if instructions[instrucPointer][0]=="acc":
        accCount+=instructions[instrucPointer][1]
        visited.add(instrucPointer)
        instrucPointer+=1
    elif instructions[instrucPointer][0]=="jmp":
        visited.add(instrucPointer)
        instrucPointer+=instructions[instrucPointer][1]
    elif instructions[instrucPointer][0]=="nop":
        visited.add(instrucPointer)
        instrucPointer+=1
print("Answer part One: ",accCount)


def changeInstruction(index):
    if instructions[index][0] == "jmp":
        instructions[index] = ("nop",instructions[index][1])
    else: instructions[index] = ("jmp",instructions[index][1])


def nowExicutes():
    visited2 = set()
    instrucPointer2 = 0
    while not instrucPointer2 in visited2:
        if instructions[instrucPointer2][0] == "acc":
            visited2.add(instrucPointer2)
            instrucPointer2 += 1
        elif instructions[instrucPointer2][0] == "jmp":
            visited2.add(instrucPointer2)
            instrucPointer2 += instructions[instrucPointer2][1]
        elif instructions[instrucPointer2][0] == "nop":
            visited2.add(instrucPointer2)
            instrucPointer2 += 1
        if instrucPointer2 == len(lines):
            return True
    return False



for v in range(len(lines)):
    if instructions[v][0]=="acc":
        continue
    changeInstruction(v)
    if nowExicutes():
        print("The bad instruction was ",lines[v]," at ",v+1)
        break
    changeInstruction(v)

visited=set()
accCount=0
instrucPointer=0
while (not instrucPointer in visited) and instrucPointer<len(lines):
    if instructions[instrucPointer][0]=="acc":
        accCount+=instructions[instrucPointer][1]
        visited.add(instrucPointer)
        instrucPointer+=1
    elif instructions[instrucPointer][0]=="jmp":
        visited.add(instrucPointer)
        instrucPointer+=instructions[instrucPointer][1]
    elif instructions[instrucPointer][0]=="nop":
        visited.add(instrucPointer)
        instrucPointer+=1
print("Answer part two: ",accCount)

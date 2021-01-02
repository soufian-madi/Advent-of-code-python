import math

with open("12.txt") as f:
    instructions  = [(l[0],int(l[1:])) for l in f.read().splitlines()]
def partOne():
    print("Start part one...")
    directions= {"E":1, "S":-1, "W":-1, "N":1}
    dirString = "ESWN"
    currentDir=0
    x,y=0,0
    for i in instructions:
        type = i[0]
        value =i[1]
        if type in "LR":
            offset = (value/90) if type == "R" else -1 * (value/90)
            currentDir= int((currentDir + offset) % 4)
        elif type in "NSEW":
            x += directions[type] * value if type in "EW" else 0
            y += directions[type] * value if type in "NS" else 0
        else:
            x += directions[dirString[currentDir]] * value if dirString[currentDir] in "EW" else 0
            y += directions[dirString[currentDir]] * value if dirString[currentDir] in "NS" else 0
    print("x = ",x,", and y= ",y)
    print("x+y= ",int(math.fabs(x)+math.fabs(y)))

def partTwo():
    print("------------\nStart part two...")
    wayPoint=[10,1]
    x,y=0,0
    for i in instructions:
        type = i[0]
        value =i[1]
        if type in "LR":
            sign=-1 if type=="L" else 1
            for j in range(int(value/90)):
                wayPoint=[sign*wayPoint[1],-1*sign*wayPoint[0]]
        elif type in "NSEW":
            if type in "NS":
                wayPoint[1] += value if type == "N" else -1*value
            else:
                wayPoint[0] += value if type == "E" else -1*value
        else:
            for i in range(value):
                x+=wayPoint[0]
                y+=wayPoint[1]

    print("x = ",x,", and y = ",y)
    print("x+y = ",int(math.fabs(x)+math.fabs(y)))

if __name__ == "__main__":
    partOne()
    partTwo()
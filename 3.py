with open("3.txt") as f:
    lines= f.read().splitlines()


def part1():
    print("Starting part one:")
    position=(0,0) #(x,y) x axis is down and y axis is to the left
    forestWitdth = len(lines[0])
    treeCount = 0
    while position[0] < len(lines):
        if lines[position[0]][position[1]]=="#":
            treeCount+=1
        position = (position[0] + 1, (position[1] + 3) % forestWitdth)
        print("pos: ",position)
    print("trees encountered along the forest: ", treeCount)

def part2():
    rightLeft=[(1,1),(3,1),(5,1),(7,1),(1,2)]
    print("Starting part two:")

    forestWitdth = len(lines[0])
    total=1
    for k,v in rightLeft:
        position = (0, 0)  # (x,y) x axis is down and y axis is to the left
        treeCount = 0
        while position[0] < len(lines):
            if lines[position[0]][position[1]] == "#":
                treeCount += 1
            position = (position[0] + v, (position[1] + k) % forestWitdth)
            print("new possiotion: ", position)
        total=total*treeCount
    print("total = ",total)




if __name__ == "__main__":
    part1()
    part2()
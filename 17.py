with open("17.txt") as f:
    lines=f.read().splitlines()
    width=len(lines)

def getNeighbors(coord):
    neigh=[]
    for a in range(-1,2,1):
        for b in range(-1,2,1):
            for c in range(-1,2,1):
                add=(coord[0]+a,coord[1]+b,coord[2]+c)
                neigh.append(add)
    neigh.remove(coord)
    return neigh

def getNeighbors4D(coord):
    neigh=[]
    for a in range(-1,2,1):
        for b in range(-1,2,1):
            for c in range(-1,2,1):
                for d in range(-1,2,1):
                    add=(coord[0]+a,coord[1]+b,coord[2]+c,coord[3]+d)
                    neigh.append(add)
    neigh.remove(coord)
    return neigh

def partOne():
    activeCoords=set()
    for x in range(width):
        for y in range(width):
            if lines[y][x]=="#":
                activeCoords.add((x,y,0))
    newActive=set()
    for cycle in range(1,7):
        for a in range(width+2*cycle):
            for b in range(width+2*cycle):
                for c in range(1+2*cycle):
                    activeNeighbours=0
                    coordinate=(a-cycle,b-cycle,c-cycle)
                    for neighbor in getNeighbors(coordinate):
                        if neighbor in activeCoords:
                            activeNeighbours+=1
                    if coordinate in activeCoords:
                        if activeNeighbours==3 or activeNeighbours==2:
                            newActive.add(coordinate)
                    else:
                        if activeNeighbours==3:
                            newActive.add(coordinate)
        activeCoords=newActive
        newActive=set()
        print("finished cycle number : ",cycle," number of active cubes:",len(activeCoords))

def partTwo():
    print("Starting part Two!")
    activeCoords = set()
    for x in range(width):
        for y in range(width):
            if lines[y][x] == "#":
                activeCoords.add((x, y, 0,0))
    newActive = set()
    for cycle in range(1, 7):
        for a in range(width + 2 * cycle):
            for b in range(width + 2 * cycle):
                for c in range(1 + 2 * cycle):
                    for d in range(1 + 2 * cycle):
                        activeNeighbours = 0
                        coordinate = (a - cycle, b - cycle, c - cycle,d-cycle)
                        for neighbor in getNeighbors4D(coordinate):
                            if neighbor in activeCoords:
                                activeNeighbours += 1
                        if coordinate in activeCoords:
                            if activeNeighbours == 3 or activeNeighbours == 2:
                                newActive.add(coordinate)
                        else:
                            if activeNeighbours == 3:
                                newActive.add(coordinate)
        activeCoords = newActive
        newActive = set()
        print("finished cycle number : ", cycle, " number of active cubes:", len(activeCoords))




if __name__ == "__main__":
  partOne()
  partTwo()


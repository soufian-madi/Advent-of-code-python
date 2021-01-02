with open('11.txt')as f:
    seatMatrix=f.read().splitlines()
def getOccupiedNeighbours(matrix,coord):
    rows=len(matrix)
    columns=len(matrix[0])
    padded=["."*columns]+matrix+["."*columns]
    padded=["."+p+"."for p in padded]
    counter=0
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            if i==0 and j==0:
                continue
            if padded[coord[0]+i+1][coord[1]+j+1]=="#":
                counter+=1
    return counter
def partOne(seatMatrix):
    hasChanged=True
    print("Start")
    while hasChanged:
        hasChanged = False
        newMatrix=seatMatrix.copy()
        for i in range (len(seatMatrix)):
            for j in range(len(seatMatrix[1])):
                numberOfNeigh=getOccupiedNeighbours(seatMatrix,(i,j))
                if seatMatrix[i][j]=="L" and numberOfNeigh==0:
                    newMatrix[i]=newMatrix[i][:j]+"#"+newMatrix[i][j+1:]
                    hasChanged=True
                elif seatMatrix[i][j]=="#" and numberOfNeigh>3:
                    newMatrix[i]=newMatrix[i][:j]+"L"+newMatrix[i][j+1:]
                    hasChanged=True

        seatMatrix=newMatrix.copy()
    occupiedCounter=0
    for s in seatMatrix:
        for c in s:
            if c =="#":
                occupiedCounter+=1
    print("Answer to part one: ",occupiedCounter)


def getOccupiedNeighbours2(matrix, coord):
    rows = len(matrix)
    columns = len(matrix[0])
    counter = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if i == 0 and j == 0:
                continue
            offset = 1
            while True:
                try:
                    if matrix[coord[0] + offset * i][coord[1] + offset * j] == "L":
                        break
                    if matrix[coord[0] + offset*i][coord[1] + offset*j] == "#" and -1<(coord[0] + offset * i)<rows and -1<(coord[1] + offset*j)<columns:
                        counter += 1
                        break
                    offset += 1
                except IndexError:
                    break

    return counter
    pass


def partTwo(seatMatrix):
    hasChanged=True
    print("Start part Two: ")
    while hasChanged:
        hasChanged = False
        newMatrix=seatMatrix.copy()
        for i in range (len(seatMatrix)):
            for j in range(len(seatMatrix[1])):
                numberOfNeigh=getOccupiedNeighbours2(seatMatrix,(i,j))
                if seatMatrix[i][j]=="L" and numberOfNeigh==0:
                    newMatrix[i]=newMatrix[i][:j]+"#"+newMatrix[i][j+1:]
                    hasChanged=True
                elif seatMatrix[i][j]=="#" and numberOfNeigh>4:
                    newMatrix[i]=newMatrix[i][:j]+"L"+newMatrix[i][j+1:]
                    hasChanged=True

        seatMatrix=newMatrix.copy()
    occupiedCounter=0
    for s in seatMatrix:
        for c in s:
            if c =="#":
                occupiedCounter+=1
    print("Answer to part two: ",occupiedCounter)


if __name__ == "__main__":
    #partOne(seatMatrix)
    partTwo(seatMatrix)





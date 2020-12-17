with open("14.txt") as f:
    lines = f.read().splitlines()
def part1(lines):
    maskZero = []
    maskOne = 0
    memory={}

    for line in lines:
        if line[:2]=="ma":
            mask=line[7:]
            maskZero = []
            maskOne = 0
            for i in range(36):
                if mask[i]=="x": continue
                if mask[i] == "0":
                    maskZero.append(35-i)
                if mask[i] == "1":
                    maskOne=maskOne|1<<(35-i)
        else:
          address=int(line.split("[")[1].split("]")[0])
          value = int(line.split("=")[1])
          value=value|maskOne
          for i in maskZero:
              value=~(1<<i)&value
          memory[address]=value

    sum=0
    for v in memory.values():
        sum+=v
    print(sum)

def part2(lines):
    memory = {}
    maskZeroOne=0
    for line in lines:
        if line[:2] == "ma":
            maskZeroOne=int(line.replace("X","0").split("=")[1],2)
            maskFloat = []
            mask = line[7:]
            for i in range(36):
                if mask[i] == "X":
                    maskFloat.append(35-i)

        else:
            address = int(line.split("[")[1].split("]")[0])
            address=address|maskZeroOne
            addressList=getPermuatuins(address,maskFloat)
            value = int(line.split("=")[1])
            for add in addressList:
                memory[add]=value
    total=sum(memory.values())
    print(total)






def getPermuatuins(value,places):
    if len(places) ==0:
        return [value]
    addresses=[]
    value1=value|(1<<places[0])
    value0=~(1<<places[0])&value
    if len(places) == 1:
        return [value0,value1]
    addresses += getPermuatuins(value1, places[1:])
    addresses+=getPermuatuins(value0,places[1:])
    return addresses






if __name__ == '__main__':

    part1(lines)
    print("^^^^part one^^^^\n\n\n")

    part2(lines)
    print("^^^^part two^^^^")
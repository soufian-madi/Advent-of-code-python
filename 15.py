with open("15.txt") as f:
    lines=f.read().splitlines()


def part1():
    print("Starting part one...")
    startingNumbers = [int(i) for i in lines[0].split(",")]
    dic={v:(-1,i+1) for i,v in enumerate(startingNumbers)}
    last=startingNumbers[-1]
    for i in range(8,2021):
        if (dic[last][0] == -1): #number is new say zero
            last =0
            dic[0] = (dic[0][1],i)
        else:
            last=dic[last][1]-dic[last][0]
            if not last in dic.keys():
                dic[last] = (-1,i)
            else: dic[last] = (dic[last][1],i)
    print("2020th number was: ",last)

def part2():
    print("Starting part two...")
    startingNumbers = [int(i) for i in lines[0].split(",")]
    dic={v:(-1,i+1) for i,v in enumerate(startingNumbers)}
    last=startingNumbers[-1]
    for i in range(8,30000000+1):

        if (dic[last][0] == -1): #number is new say zero
            last =0
            dic[0] = (dic[0][1],i)
        else:
            last=dic[last][1]-dic[last][0]
            if not last in dic.keys():
                dic[last] = (-1,i)
            else: dic[last] = (dic[last][1],i)
    print("30000000th number was: ",last)






if __name__ == "__main__":
    part1()
    part2()
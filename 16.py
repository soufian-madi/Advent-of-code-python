with open("16.txt") as f:
    lines = f.read().split("\n\n")
    fields = lines[0]
    myTicket = lines[1]
    nearbyTickets = lines[2]

def partOne():
    intervals=[]
    for line in fields.splitlines():
        for i in line.split(": ")[1].split(" or "):
            intervals.append(i)
    intervalDic ={int(i.split("-")[0]):int(i.split("-")[1]) for i in intervals}
    tickets =nearbyTickets.splitlines()[1:]
    tser=0
    for t in tickets:
        numbers=[int(n) for n in t.split(",")]
        for n in numbers:
            isInAnyInterval=False
            for k in intervalDic.keys():
                if  k<=n<=intervalDic[k]:
                    isInAnyInterval=True
            if not isInAnyInterval:
                tser+=n
    print("ticket error scanning rate is: ", tser)
def partTwo():
    fieldIntervaldict={}
    for line in fields.splitlines():
        fieldIntervaldict[line.split(": ")[0]]=[]
        for i in line.split(": ")[1].split(" or "):
            fieldIntervaldict[line.split(": ")[0]].append((int(i.split("-")[0]),int(i.split("-")[1])))
    tickets =[[int(n) for n in i.split(",")] for i in nearbyTickets.splitlines()[1:]]
    validTickets=[]
    for t in tickets:
        valid=True
        for n in t:
             if not any(any(interval[0]<=n<=interval[1]for interval in v)  for k,v in fieldIntervaldict.items()):
                   valid =False
        if valid:
             validTickets.append(t)
    possebilities={index:list(fieldIntervaldict.keys())for index,key in enumerate(fieldIntervaldict)}

    for t in validTickets:
        for index,n in enumerate(t):
            for k,v in fieldIntervaldict.items():
                if (not (v[0][0]<=n<=v[0][1] or v[1][0]<=n<=v[1][1])) and (k in possebilities[index]):
                  possebilities[index].remove(k)
    for k in possebilities:
        print(k,"has",len(possebilities[k]),"possibiliteis:",possebilities[k])
    print("---------------------------------------------")
    changed = True
    while changed:
        changed = False
        for index,p in possebilities.items():
            if len(p)==1:
                for ii in possebilities:
                    if ii!=index and p[0] in possebilities[ii]:
                        possebilities[ii].remove(p[0])
                        changed=True
    for k in possebilities:
        print(k, "has", len(possebilities[k]), "possibiliteis:", possebilities[k])
    myTicketnumbers=[int(s) for s in myTicket.splitlines()[1].split(",")]
    answer=1
    for index,field in possebilities.items():
        if "departure" in field[0]:
            answer*=myTicketnumbers[index]
    print(answer)






if __name__ == "__main__":
    partOne()
    partTwo()

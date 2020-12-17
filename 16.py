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
    intervals=[]
    for line in fields.splitlines():
        for i in line.split(": ")[1].split(" or "):
            intervals.append(i)
    fieldIntervaldict={}
    for i,line in enumerate(fields.splitlines()):
        fieldIntervaldict[line.split(": ")[0]]=(intervals[2*i],intervals[2*i+1])
    print(fieldIntervaldict)
    intervalDic ={int(i.split("-")[0]):int(i.split("-")[1]) for i in intervals}
    tickets =nearbyTickets.splitlines()[1:]
    invalidInexes=set()
    tser=0
    for i,t in enumerate(tickets):
        numbers=[int(n) for n in t.split(",")]
        for n in numbers:
            isInAnyInterval=False
            for k in intervalDic.keys():
                if  k<=n<=intervalDic[k]:
                    isInAnyInterval=True
            if not isInAnyInterval:
                tser+=n
                invalidInexes.add(i)
    for i,t in enumerate(tickets):
        if i in invalidInexes: continue
        for n in t.split(","):
            candidates=[]
            for k in fieldIntervaldict.keys():
                if int(fieldIntervaldict[k][0].split("-")[0])<=int(n)<=int(fieldIntervaldict[k][0].split("-")[1]):
                    candidates.append(k)
                    print(n,"is valid vor ", k)







if __name__ == "__main__":
    partOne()
    partTwo()

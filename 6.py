with open("6.txt") as f:
    groups=f.read().split("\n\n")

    setList=[]
    for g in groups:
        setList.append(set("".join(g.split("\n"))))
    sum=sum([len(i) for i in setList])
    print("Part one : ",sum)
    ############Start of part Two############
    totalsum=0
    for g in groups:
        members=g.splitlines()
        disqualified=set()
        for person1 in members:
            for person2 in members:
                for letter in person1:
                    if not letter in person2:
                        disqualified.add(letter)
        print(disqualified)
        for c in members[0]:
            if not c in disqualified:
                totalsum+=1
    print("Part two : ",totalsum)

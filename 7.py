with open("7.txt") as f:
    rules=f.read().splitlines()
    rules=[r[:-1] for r in rules]
ruleDic={" ".join(rule.split(" ")[:2]): rule.split("contain ")[1].split(", ") for rule in rules}

for k in ruleDic.keys():
    if 'no other bags' in ruleDic[k]:
        continue
    ruleDic[k] =[e[2:-5] if e[0]!="1" else e[2:-4] for e in ruleDic[k] ]

changed=True
validBags=set()
validBags.add("shiny gold")
while changed:
    newValids=set()
    for k,v in ruleDic.items():
        for color in v :
            if color in validBags and not k in validBags:
                newValids.add(k)
    changed=newValids
    validBags=set.union(validBags,newValids)
validBags.remove("shiny gold")

print("\nAnswer part one: ",len(validBags))

####Part 2####
ruleDic={" ".join(rule.split(" ")[:2]): rule.split("contain ")[1].split(", ") for rule in rules}

for k in ruleDic.keys():
    if 'no other bags' in ruleDic[k]:
        continue
    ruleDic[k] =[(e[2:-5],int(e[0])) if e[0]!="1" else (e[2:-4],int(e[0])) for e in ruleDic[k] ]
def bagsCount(color):
    if "no other bags" in ruleDic[color]:
        return 1
    totalBags = 0
    for tup in ruleDic[color]:
        totalBags+=(tup[1]*bagsCount(tup[0]))
    print("for ",color," returning: ",totalBags)
    return totalBags+1
print("Answer part two: ", bagsCount("shiny gold")-1)


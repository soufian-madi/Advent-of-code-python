with open("5.txt") as f:
    idss=f.read().splitlines()
    rows, colums=[id[:7] for id in idss],[id[7:] for id in idss]

def parseRow(str):
    bits = str.replace("B","1").replace("F","0")
    return int(bits,2)
def parseColumn(str):
    bits = str.replace("R", "1").replace("L", "0")
    return int(bits, 2)
print("Starting part one:")
ids=[parseColumn(colums[i])+parseRow(rows[i])*8 for i in range(len(colums))]
print("max id is: ", max(ids))

print("--------------\nStarting part two:")
ids.sort()
print(ids)
for index,id in enumerate(ids):
    if id !=ids[index+1]-1:
        print("my id is: ",id+1)
        break


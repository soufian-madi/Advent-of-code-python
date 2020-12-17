with open("4.txt") as f:
    lines= f.read().splitlines()


def part1():
    #byr = iyr = eyr = hgt = hcl = ecl = pid = False
    reference=["byr",'iyr','eyr','hgt','hcl','ecl','pid']
    descriptors = []
    validcounter=0
    for line in lines:
        if not line:
            validcounter=validcounter+1 if all(elem in descriptors for elem in reference) else validcounter
            print(descriptors,"was: ","valid" if all(elem in descriptors for elem in reference) else "invalid")
            descriptors=[]
            continue
        pairs=line.split(" ")
        for pair in pairs:
            descriptors.append(pair.split(":")[0])
    print(validcounter+1, " valid passports got identified")



def part2():
    print("Starting part two")
    reference=["byr",'iyr','eyr','hgt','hcl','ecl','pid']
    eyeColors=["amb","blu","brn","gry","grn","hzl","oth"]
    descriptors = []
    validcounter=0
    entries={}
    for line in lines:
        if not line:
            hasNeccaryValues=all(elem in descriptors for elem in reference)
            allValuesAreValid=False
            if hasNeccaryValues:
                validByrIyr=2003>int(entries["byr"])>=1920 and 2021>int(entries["iyr"])>=2010
                valideyr=2031>int(entries["eyr"])>=2020
                validHcl=entries["hcl"][0]=="#" and len(entries["hcl"])==7
                validEcl=entries["ecl"] in eyeColors
                validPid=len(entries["pid"])==9 and entries["pid"].isdigit()
                validHgt= False
                if entries["hgt"][-2:]=="cm" and entries["hgt"][:-2].isdigit() and 149<int(entries["hgt"][:-2])<194:
                    validHgt=True
                if entries["hgt"][-2:]=="in" and entries["hgt"][:-2].isdigit() and 58<int(entries["hgt"][:-2])<77:
                    validHgt=True
                allValuesAreValid=all([validByrIyr,valideyr,validHcl,validEcl,validPid,validHgt])
            isValid =hasNeccaryValues and allValuesAreValid
            validcounter=validcounter+1 if isValid else validcounter
            print("for ",descriptors,"was: ",all(elem in descriptors for elem in reference))
            print(entries)
            entries={}
            descriptors=[]
            continue
        pairs=line.split(" ")
        for pair in pairs:
            entries[pair.split(":")[0]]=pair.split(":")[1]
            descriptors.append(pair.split(":")[0])
    print(validcounter+1, " valid passports got identified")







if __name__ == "__main__":
    part1()
    part2()
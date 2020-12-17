with open("2.txt") as f:
    lines = f.read().splitlines()


def partOne():
    validCouter = 0
    for line in lines:
        atLeast = int(line.split("-")[0])
        atMost = int(line.split(" ")[0].split("-")[1])
        letter = line.split(" ")[1][0]
        password = line.split(" ")[2]
        if atLeast <= password.count(letter) <= atMost:
            print("valid")
            validCouter += 1
    print(validCouter, "  valid passwords ya'll")


def partTwo():
    validCouter = 0
    for line in lines:
        firstIndex = int(line.split("-")[0])-1
        Secondindex = int(line.split(" ")[0].split("-")[1]) - 1
        letter = line.split(" ")[1][0]
        password = line.split(" ")[2]
        if (password[firstIndex]==letter) ^ (password[Secondindex]==letter) :
            print("valid")
            validCouter += 1
    print(validCouter, "  valid passwords ya'll")


if __name__ == '__main__':
    #partOne()
    partTwo()


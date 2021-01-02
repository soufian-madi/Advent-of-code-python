with open("9.txt") as f:
    numbers=[int(l) for l in f.read().splitlines()]
preamble=numbers[:25]
candidates=numbers[25:]
def isValid(lst):
    candidate=lst[25]
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if i==j:
                continue
            if lst[i]+lst[j]==candidate:
                return True
    return False
notFound=True
currentIndex=25
while notFound:
    if isValid(numbers[currentIndex-25:currentIndex+1]):
        currentIndex+=1
        continue
    else: notFound=False
firstInvalid=numbers[currentIndex]
print("Answer to part One : ",firstInvalid)

firstIndex=0
lastIndex=1
while True:
    summ = numbers[firstIndex] + numbers[firstIndex + 1]
    if summ==firstInvalid:
        break
    while summ<firstInvalid:
        lastIndex+=1
        summ+=numbers[lastIndex]
        if summ == firstInvalid:
            break
    if summ == firstInvalid:
        break
    firstIndex+=1
    lastIndex=firstIndex+1



sumArray=numbers[firstIndex:lastIndex+1]
print("Answer to part two: ",max(sumArray)+min(sumArray))



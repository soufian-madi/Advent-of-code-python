with open("10.txt") as f:
    numbers = sorted([int(i) for i in f.read().splitlines()])
    numbers=[0]+numbers+[numbers[-1]+3]
onesCounter=sum([1 for i in range(len(numbers)-1) if numbers[i+1]-numbers[i] ==1])
threesCounter=sum([1 for i in range(len(numbers)-1) if numbers[i+1]-numbers[i] ==3])
twosCounter=sum([1 for i in range(len(numbers)-1) if numbers[i+1]-numbers[i] ==2])
print("Answer Part One: ",onesCounter*threesCounter)
print("Starting part two...")
print(numbers)
start =0
sublists= []
combinations=1
for i in range(len(numbers)-1):
    if numbers[i+1]-numbers[i]==3:
        sublists.append(numbers[start:i+1])
        if len(sublists[-1]) ==3:
            combinations*=2
        elif len(sublists[-1]) ==4:
            combinations*=4
        elif len(sublists[-1]) ==5:
            combinations*=7
        start=i+1
print("Answer Part Two:  ",combinations)



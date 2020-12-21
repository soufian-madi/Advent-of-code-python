import re
import emoji
with open("18.txt") as f:
    equations=[i.replace(" ","") for i in f.read().splitlines()]
patern = re.compile(r'\(\d+([+*]\d+)+\)')
solutions=[0 for i in range(len(equations))]
def parseExpression(expr):
    numbers=re.split("\+|\*",expr)
    operators=re.compile(r"[\*\+]").findall(expr)
    answer=int(numbers[0])
    for i,op in enumerate(operators):
        if op =="+":
            answer=answer+int(numbers[i+1])
        else:
            answer=answer*int(numbers[i+1])

    return str(answer)


def partOne():
    for index,eq in enumerate(equations):
        solutions[index] = eq
        while len(patern.findall(eq)) > 0:
            matches = patern.finditer(eq)
            for match in matches:
                replacement = parseExpression(match.group(0)[1:-1])
                eq=eq.replace(match.group(0),replacement)
            solutions[index]=eq
        solutions[index]=parseExpression(solutions[index])
    print("sum for part one is: ",sum([int(i) for i in solutions]))

def parseExpression2(expr):
    if not "+" in expr:
        return parseExpression(expr)
    firstPlus = [i for i, c in enumerate(expr) if c == "+"][0]
    pluseq=re.compile(r"\d+\+\d+")
    numbers=pluseq.findall(expr)[0].split("+")
    expr=expr[:firstPlus-len(numbers[0])]+str(int(numbers[0])+int(numbers[1]))+expr[firstPlus+len(numbers[1])+1:]
    return parseExpression2(expr)
def partTwo():
    solutions=[0 for i in range(len(equations))]
    for index, eq in enumerate(equations):
        solutions[index] = eq
        while len(patern.findall(eq)) > 0:
            matches = patern.finditer(eq)
            for match in matches:
                replacement = parseExpression2(match.group(0)[1:-1])
                eq = eq.replace(match.group(0), replacement)
            solutions[index] = eq
        solutions[index] = parseExpression2(solutions[index])
    print("sum for part two is: ", sum([int(i) for i in solutions]))

if __name__ == "__main__":
    partOne()
    partTwo()





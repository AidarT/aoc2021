from functools import reduce
import re


def posCalc(inst, pos):
    match inst[0]:
        case "forward":
            return [pos[0] + inst[1], pos[1]]
        case "down":
            return [pos[0], pos[1] + inst[1]]
        case "up":
            return [pos[0], pos[1] - inst[1]]


def aimedPosCalc(inst, pos):
    match inst[0]:
        case "forward":
            return [pos[0] + inst[1], pos[1] + pos[2] * inst[1], pos[2]]
        case "down":
            return [pos[0], pos[1], pos[2] + inst[1]]
        case "up":
            return [pos[0], pos[1], pos[2] - inst[1]]


with open('C:/Users/User/Documents/input.txt') as f:
    instruction = list(map(lambda a: re.findall(r'[a-z]+|\d', a), f.read().split('\n')))
    instruction = [[inst[0], int(inst[1])] for inst in instruction]
f.close()

part1 = reduce(lambda prev, cur: posCalc(cur, prev), instruction, [0, 0])
part1 = part1[0] * part1[1]

part2 = reduce(lambda prev, cur: aimedPosCalc(cur, prev), instruction, [0, 0, 0])
part2 = part2[0] * part2[1]

print(str(part1) + " " + str(part2))

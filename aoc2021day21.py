import math
import re
import copy

with open('C:/Users/User/Documents/input.txt') as f:
    pos = list(map(lambda a: list(map(lambda b: int(b), re.findall(r'\d+', a))), f.read().split('\n')))
    pos_p2 = copy.deepcopy(pos)
f.close()

scores = [0, 0]
die = 1
amount = 0
while True:
    amount += 3
    new_pos = pos[0][1] + (die * 3 + 3) % 10
    pos[0][1] = new_pos if new_pos <= 10 else new_pos % 10
    scores[0] += pos[0][1]
    if scores[0] >= 1000:
        lost = 1
        break
    die += 3
    amount += 3
    new_pos = pos[1][1] + (die * 3 + 3) % 10
    pos[1][1] = new_pos if new_pos <= 10 else new_pos % 10
    scores[1] += pos[1][1]
    die += 3
    if scores[1] >= 1000:
        lost = 0
        break

part1 = amount * scores[lost]


def quantum_dice(pos, scores, universes, die, player):
    new_pos = pos[player][1] + die
    pos[player][1] = new_pos if new_pos <= 10 else new_pos % 10
    scores[player] += pos[player][1]
    if scores[player] >= 21:
        universes[player] += 1
        return
    for i in range(3, 10):
        quantum_dice(pos.copy(), scores.copy(), universes, i, 1-player)


scores = [0, 0]
universes = [0, 0]
for i in range(3, 10):
    quantum_dice(pos_p2.copy(), scores.copy(), universes, i, 0)

part2 = max(universes)

print(str(part1) + ' ' + str(part2))

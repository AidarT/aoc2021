from functools import reduce
import re

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = f.read().split('\n\n')
f.close()

dots = list(map(lambda b: list(map(lambda a: int(a), re.findall(r'\d+', b))), my_input[0].split('\n')))
folds = list(map(lambda b: re.findall(r'[x|y]=\d+', b), my_input[1].split('\n')))
folds = [(fold[0].split('=')[0], int(fold[0].split('=')[1])) for fold in folds]

max_x = max([coord[0] for coord in dots])
max_y = max([coord[1] for coord in dots])
paper = [[0 for x in range(0, max_x + 1)] for y in range(0, max_y + 1)]
for x, y in dots:
    paper[y][x] = 1

part1 = 0
for type_, coord in folds:
    if type_ == 'y':
        fold1 = list(reversed(paper[:coord]))
        fold2 = paper[coord + 1:]
        paper = list(reversed([[dot | (fold2[y][x] if y < len(fold2) else 0) for x, dot in enumerate(line)]
                               for y, line in enumerate(fold1)]))
    else:
        fold1 = [line[:coord] for line in paper]
        fold2 = [list(reversed(line[coord + 1:])) for line in paper]
        paper = [[dot1 | dot2 for dot1, dot2 in zip(line1, line2)] for line1, line2 in zip(fold1, fold2)]
    if part1 == 0:
            part1 = reduce(lambda prev, cur: prev + cur.count(1), paper, 0)

print(str(part1) + " Часть 2:")
paper = [["#" if dot == 1 else " " for dot in line] for line in paper]
for line in paper:
    print(('').join(line))

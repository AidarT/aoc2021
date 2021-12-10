from functools import reduce

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = f.read().split('\n')
f.close()

chars = {')': '(', ']': '[', '}': '{', '>': '<'}
scores_p1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
part1 = 0
ind_del = []
for ind, line in enumerate(my_input):
    while True:
        len1 = len(line)
        line = line.replace("()", "").replace("[]", "").replace("{}", "").replace("<>", "")
        if len1 == len(line):
            break
    my_input[ind] = line
    indexes = [(i, ch) for i, ch in enumerate(line) if ch in "}])>"]
    if len(indexes) > 0:
        if line[indexes[0][0] - 1] != chars[indexes[0][1]]:
            part1 += scores_p1[indexes[0][1]]
            ind_del.append(ind)

ind_del.reverse()
for ind in ind_del:
    del my_input[ind]

scores_p2 = {')': 1, ']': 2, '}': 3, '>': 4}
chars = {v: k for k, v in chars.items()}
part2 = []
for line in my_input:
    line = line[::-1]
    part2.append(reduce(lambda prev, cur: prev * 5 + scores_p2[chars[cur]], line, 0))

part2 = sorted(part2)[int((len(part2)-1)/2)]

print(str(part1) + " " + str(part2))

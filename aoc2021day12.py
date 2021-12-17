import copy

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: a.split('-'), f.read().split('\n')))
f.close()

caves = {}
for begin, end in my_input:
    if begin not in caves:
        caves[begin] = [end]
    else:
        caves[begin].append(end)
    if end not in caves and end != 'end' and begin != 'start':
        caves[end] = [begin]
    elif end != 'end' and begin != 'start':
        caves[end].append(begin)

for_del = [cave for cave in caves if len(caves[cave]) == 1 and caves[cave][0].islower()]
caves_part2 = copy.deepcopy(caves)
for i in for_del:
    del caves[caves[i][0]][caves[caves[i][0]].index(i)]
    del caves[i]


def calc_paths(paths, caves, start, path, flag=False, count=False):
    path_prev = path
    count_prev = count
    for cave in caves[start]:
        path = path_prev
        count = count_prev
        if not flag and cave.islower() and cave in path:
            continue
        if flag and cave.islower() and cave in path and (count or cave == "start"):
            continue
        path += ',' + cave
        if path.split(',').count(cave) > 1 and cave.islower():
            count = True
        if cave != 'end':
            calc_paths(paths, caves, cave, path, flag, count)
        else:
            if path not in paths:
                paths.append(path)


paths = []
calc_paths(paths, caves, 'start', 'start')
part1 = len(paths)

paths.clear()
calc_paths(paths, caves_part2, 'start', 'start', True)
part2 = len(paths)

print(str(part1) + " " + str(part2))

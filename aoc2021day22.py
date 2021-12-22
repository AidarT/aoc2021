import re

with open('C:/Users/User/Documents/input.txt') as f:
    steps = [[line.split(' ')[0]] + list(map(lambda a: int(a), re.findall(r'-?\d+', line)))
                for line in f.read().split('\n')]
f.close()

cubes = {}
borders = [-50, 50]

for state, x_min, x_max, y_min, y_max, z_min, z_max in steps:
    if (x_min < borders[0] and x_max > borders[1]) or (y_min < borders[0] and y_max > borders[1]) \
        or (z_min < borders[0] and z_max > borders[1]):
        continue
    for x in range(x_min, x_max+1):
        if borders[0] <= x <= borders[1]:
            for y in range(y_min, y_max + 1):
                if borders[0] <= y <= borders[1]:
                    for z in range(z_min, z_max + 1):
                        if borders[0] <= z <= borders[1]:
                            if state == "on" and (x, y, z) not in cubes:
                                cubes[x, y, z] = state
                            elif state == "off" and (x, y, z) in cubes:
                                del cubes[x, y, z]

part1 = len(cubes)

# x_min = min([line[1] for line in steps])
# y_min = min([line[3] for line in steps])
# z_min = min([line[5] for line in steps])
# x_max = max([line[2] for line in steps])
# y_max = max([line[4] for line in steps])
# z_max = max([line[6] for line in steps])
# cubes = {(x, y, z): "off" for x in range(x_min, x_max+1) for y in range(y_min, y_max+1) for z in range(z_min, z_max+1)}


def crossing_check(cube1, cube2):
    state1, x1_min, x1_max, y1_min, y1_max, z1_min, z1_max = cube1
    state2, x2_min, x2_max, y2_min, y2_max, z2_min, z2_max = cube2
    cross_check = (x1_min <= x2_min <= x1_max or x1_min <= x2_max <= x1_max) and \
                  (y1_min <= y2_min <= y1_max or y1_min <= y2_max <= y1_max) and \
                  (z1_min <= z2_min <= z1_max or z1_min <= z2_max <= z1_max)
    if cross_check:
        x_min = max(x1_min, x2_min)
        x_max = min(x1_max, x2_max)
        y_min = max(y1_min, y2_min)
        y_max = min(y1_max, y2_max)
        z_min = max(z1_min, z2_min)
        z_max = min(z1_max, z2_max)
        return [state2, x_min, x_max, y_min, y_max, z_min, z_max]
    else:
        return 0


def calc_cubes(cube):
    state, x_min, x_max, y_min, y_max, z_min, z_max = cube
    return abs(x_max - x_min + 1) * abs(y_max - y_min + 1) * abs(z_max - z_min + 1)


crossings = [[[] for line in steps] for line in steps]
for i, [state1, x1_min, x1_max, y1_min, y1_max, z1_min, z1_max] in enumerate(steps):
    for j, line in enumerate(crossings):
        if i == j:
            crossings[i][i] = abs(x1_max - x1_min + 1) * abs(y1_max - y1_min + 1) * abs(z1_max - z1_min + 1)
        else:
            state2, x2_min, x2_max, y2_min, y2_max, z2_min, z2_max = steps[j]
            cross_check = (x1_min <= x2_min <= x1_max or x1_min <= x2_max <= x1_max) and \
                          (y1_min <= y2_min <= y1_max or y1_min <= y2_max <= y1_max) and \
                          (z1_min <= z2_min <= z1_max or z1_min <= z2_max <= z1_max)
            if cross_check:
                x_min = max(x1_min, x2_min)
                x_max = min(x1_max, x2_max)
                y_min = max(y1_min, y2_min)
                y_max = min(y1_max, y2_max)
                z_min = max(z1_min, z2_min)
                z_max = min(z1_max, z2_max)
                crossings[i][j] = [state2, x_min, x_max, y_min, y_max, z_min, z_max]
                # if state2 == 'on':
                #     crossings[i][j] = abs(x2_max - x2_min + 1) * abs(y2_max - y2_min + 1) * abs(z2_max - z2_min + 1) \
                #                       - abs(x_max - x_min + 1) * abs(y_max - y_min + 1) * abs(z_max - z_min + 1)
                # else:
                #     crossings[i][j] = - abs(x_max - x_min + 1) * abs(y_max - y_min + 1) * abs(z_max - z_min + 1)
            else:
                crossings[i][j] = 0


part2 = crossings[0][0]
for i, crossing in enumerate(crossings[0]):
    if i > 0:
        if crossing != 0:
            state_cr, x_cr_min, x_cr_max, y_cr_min, y_cr_max, z_cr_min, z_cr_max = crossing
            cubes_cr = abs(x_cr_max - x_cr_min + 1) * abs(y_cr_max - y_cr_min + 1) * abs(z_cr_max - z_cr_min + 1)
            if state_cr == "on":
                part2 += crossings[i][i] - cubes_cr
            else:
                part2 -= cubes_cr
                for j in range(1, i):
                    if crossings[j][i] != 0:
                        cross = crossing_check(crossings[j][i], crossing)
                        part2 = part2 - calc_cubes(crossings[j][i]) + (0 if cross == 0 else calc_cubes(cross))
        else:
            part2 += crossings[i][i]

# tmp = sum(crossings[0])
cubes = 0
for i, state, x_min, x_max, y_min, y_max, z_min, z_max in enumerate(steps):
    if i == 0:
        cubes += abs(x_max - x_min) * abs(y_max - y_min) * abs(z_max - z_min)
    else:
        cubes_off = [line for j, line in enumerate(steps) if line[0] == 'off' and j > i]


part2 = 0

print(str(part1) + ' ' + str(part2))

import re

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = f.read().split('\n')
f.close()
coords = [[int(num) for num in re.findall(r'\d+', line)] for line in my_input]


def map_build(coords, flag):
    map = {}
    for x1, y1, x2, y2 in coords:
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    map[(x, y)] = 1 if (x, y) not in map else map[(x, y)] + 1
        elif flag and min(y1, y2) + abs(x1 - x2) == max(y1, y2):
            y = y1
            x_step = 1 if x1 < x2 else -1
            for x in range(x1, x2 + x_step, x_step):
                map[(x, y)] = 1 if (x, y) not in map else map[(x, y)] + 1
                y += 1 if y1 < y2 else -1
    return len([cross for cross in map.values() if cross > 1])

part1 = map_build(coords, False)
part2 = map_build(coords, True)

print(str(part1) + " " + str(part2))

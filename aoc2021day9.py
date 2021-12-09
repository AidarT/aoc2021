import math
import re

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(map(lambda b: int(b), re.findall(r'\d', a))), f.read().split('\n')))
f.close()

low_points = {}
for y, nums in enumerate(my_input):
    for x, num in enumerate(nums):
        if (x + 1 < len(nums) and nums[x + 1] <= num)\
                or (x - 1 >= 0 and nums[x - 1] <= num)\
                or (y + 1 < len(my_input) and my_input[y + 1][x] <= num)\
                or (y - 1 >= 0 and my_input[y - 1][x] <= num):
            continue
        low_points[(x, y)] = num

part1 = sum(low_points.values()) + len(low_points)

moves = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
backMoves = {1: 2, 2: 1, 3: 4, 4: 3}
map_ = {(x, y): v for y, line in enumerate(my_input) for x, v in enumerate(line)}


def nexMoveChoice(move, cur_coord, map_):
    new_coord = cur_coord[0] + moves[move][0], cur_coord[1] + moves[move][1]
    if new_coord in map_ and (map_[new_coord] != 9):
        return move
    return 0


def basin_calc(move, cur_coord, map_, path):
    new_coord = cur_coord[0] + moves[move][0], cur_coord[1] + moves[move][1]
    if new_coord not in path and new_coord in map_ and (map_[new_coord] != 9):
        path[new_coord] = 1
        cur_coord = new_coord
        old_dir = backMoves[move]
        for i in range(1, 5, 1):
            if i != old_dir:
                move = nexMoveChoice(i, cur_coord, map_)
                if move != 0:
                    basin_calc(move, cur_coord, map_, path)


basins = []
for coord, h in low_points.items():
    basin = {coord: 1}
    for i in range(1, 5, 1):
        basin_calc(i, coord, map_, basin)
    basins.append(basin)

part2 = math.prod(sorted([len(b.values()) for b in basins], reverse=True)[0:3])

print(str(part1) + " " + str(part2))

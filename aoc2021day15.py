import re

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(map(lambda b: int(b), re.findall(r'\d', a))), f.read().split('\n')))
f.close()

moves = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
map_ = {(x, y): v for y, line in enumerate(my_input) for x, v in enumerate(line)}
aim = (max([coord[0] for coord in map_.keys()]), max([coord[1] for coord in map_.keys()]))


def A_star_search(map_, aim):
    # алгоритм A*
    queue = [[(0, 0), 0]]
    came_from = {(0, 0): None}
    costs = {(0, 0): 0}
    while len(queue) != 0:
        priorities = [el[1] for el in queue]
        cur_node = queue.pop(priorities.index(min(priorities)))[0]
        if cur_node == aim:
            return costs[aim]
        for move in range(1, 5, 1):
            next_node = cur_node[0] + moves[move][0], cur_node[1] + moves[move][1]
            if next_node not in map_: continue
            new_cost = costs[cur_node] + map_[next_node]
            if next_node not in costs or new_cost < costs[next_node]:
                costs[next_node] = new_cost
                queue.append([next_node, new_cost])
                came_from[next_node] = cur_node


part1 = A_star_search(map_, aim)

new_input = my_input.copy()
for i, line in enumerate(my_input):
    new_line = line.copy()
    for iter in range(1, 5):
        new_line = [num + 1 if num + 1 < 10 else 1 for num in new_line]
        new_input[i] = [*new_input[i], *new_line]
my_input = new_input.copy()
for iter in range(1, 5):
    for line in my_input:
        new_line = [num + iter if num + iter < 10 else num + iter - 9 for num in line]
        new_input.append(new_line)

map_ = {(x, y): v for y, line in enumerate(new_input) for x, v in enumerate(line)}
aim = (max([coord[0] for coord in map_.keys()]), max([coord[1] for coord in map_.keys()]))
part2 = A_star_search(map_, aim)

print(str(part1) + str(part2))

import re

with open('C:/Users/User/Documents/input.txt') as f:
    en_map = list(map(lambda a: list(map(lambda b: int(b), re.findall(r'\d', a))), f.read().split('\n')))
    flashed = {(x,y):0 for y,line in enumerate(en_map) for x,v in enumerate(line)}
    energy = {(x,y):v for y,line in enumerate(en_map) for x,v in enumerate(line)}
f.close()

moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def calc_flashes(energy, flashed, amount, turns, max_turns, part):
    if turns == max_turns and part == 1:
        return amount
    if part == 2 and [v for v in flashed.values()].count(1) == len(flashed.values()):
        return turns
    for coord in flashed:
        flashed[coord] = 0
    for coord in energy:
        if flashed[coord] != 1:
            energy[coord] += 1
            en_map[coord[1]][coord[0]] += 1
            if energy[coord] > 9:
                amount += 1
                energy[coord] = 0
                en_map[coord[1]][coord[0]] = 0
                flashed[coord] = 1
                amount = flash(energy, flashed, coord, amount)
    turns += 1
    amount = calc_flashes(energy, flashed, amount, turns, max_turns, part)
    return amount
                

def flash(energy, flashed, coord, amount):    
    for move in moves:
        new_coord = (coord[0] + move[0], coord[1] + move[1])
        if new_coord in energy:
            if flashed[new_coord] != 1:
                energy[new_coord] += 1
                en_map[new_coord[1]][new_coord[0]] += 1
                if energy[new_coord] > 9:
                    amount += 1
                    energy[new_coord] = 0
                    en_map[new_coord[1]][new_coord[0]] = 0
                    flashed[new_coord] = 1
                    amount = flash(energy, flashed, new_coord, amount)
    return amount

part1 = calc_flashes(energy, flashed, 0, 0, 100, 1)

part2 = calc_flashes(energy, flashed, 0, 0, 1000, 2)

print(str(part1) + " " + str(part2))

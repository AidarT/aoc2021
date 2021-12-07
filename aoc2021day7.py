from functools import reduce

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: int(a), f.read().split(',')))
f.close()


def calc_fuel(pos, flag):
    min_i, max_i = min(pos), max(pos)
    counts = {}
    for i in range(min_i, max_i + 1, 1):
        if not flag:
            counts[i] = reduce(lambda prev, cur: prev + abs(cur - i), pos, 0)
        else:
            counts[i] = reduce(lambda prev, cur: prev + sum([num for num in range(1, abs(cur - i) + 1)]), pos, 0)
    return min(counts.values())


part1 = calc_fuel(my_input, 0)
part2 = calc_fuel(my_input, 1)

print(str(part1) + " " + str(part2))

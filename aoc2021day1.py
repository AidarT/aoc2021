from functools import reduce

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: int(a), f.read().split('\n')))
f.close()

part1 = reduce(lambda prev, cur: [prev[0] + 1, cur] if cur > prev[1] else [prev[0], cur], my_input, [0, my_input[0]])[0]

sums = [my_input[i] + my_input[i + 1] + my_input[i + 2] for i in range(0, len(my_input) - 2, 1)]

part2 = reduce(lambda prev, cur: [prev[0] + 1, cur] if cur > prev[1] else [prev[0], cur], sums, [0, sums[0]])[0]

print(str(part1) + " " + str(part2))

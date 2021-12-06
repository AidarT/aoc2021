from functools import reduce

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: int(a), f.read().split(',')))
f.close()


def cycle(data, cycles):
    coefs = []
    school = []
    for fish in data:
        if fish not in school:
            count = data.count(fish)
            school.append(fish)
            coefs.append(count)
    data = list(dict.fromkeys(data))
    while cycles > 0:
        count = data.count(0)
        if count > 1:
            while count > 1:
                index1 = data.index(0)
                index2 = data.index(0, index1 + 1)
                coefs[index1] = coefs[index1] + coefs[index2]
                del coefs[index2]
                del data[index2]
                count -= 1
        index = 0 if count == 0 else data.index(0)
        data = [num-1 if num > 0 else 6 for num in data]
        if count > 0:
            data.append(8)
            coefs.append(coefs[index])
        cycles -= 1
    coefs = [num - 1 for num in coefs if num > 1]
    amount = reduce(lambda prev, cur: prev + cur, coefs, 0)
    return len(data) + amount


part1 = cycle(my_input.copy(), 80)
part2 = cycle(my_input.copy(), 256)

print(str(part1) + " " + str(part2))

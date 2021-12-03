import re

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(map(lambda a: int(a), re.findall(r'.', a))), f.read().split('\n')))
f.close()


def find_rate_p2(input, flag):
    temp_input = input.copy()
    rate_str = ""
    for x in range(0, len(input[0]), 1):
        zero_count = 0
        one_count = 0
        if x > 0:
            for y in range(len(temp_input) - 1, -1, -1):
                for i in range(0, x, 1):
                    if temp_input[y][i] != int(rate_str[i]):
                        temp_input.pop(y)
                        break
        if len(temp_input) == 1:
            temp_input[0] = [str(int) for int in temp_input[0]]
            rate_str = "".join(temp_input[0])
            return rate_str
        for y in range(0, len(temp_input), 1):
            if temp_input[y][x] == 1:
                one_count = one_count + 1
            else:
                zero_count = zero_count + 1
        if one_count >= zero_count:
            rate_str = rate_str + ("1" if flag == 1 else "0")
        else:
            rate_str = rate_str + ("0" if flag == 1 else "1")
    return rate_str


gamma_rate = ""
epsilon_rate = ""
for x in range(0, my_input[0].__len__(), 1):
    zero_count = 0
    one_count = 0
    for y in range(0, my_input.__len__(), 1):
        if my_input[y][x] == 1:
            one_count = one_count + 1
        else:
            zero_count = zero_count + 1
    if one_count > zero_count:
        gamma_rate = gamma_rate + "1"
        epsilon_rate = epsilon_rate + "0"
    else:
        gamma_rate = gamma_rate + "0"
        epsilon_rate = epsilon_rate + "1"

part1 = int(gamma_rate, 2) * int(epsilon_rate, 2)

O2_rate = find_rate_p2(my_input, 1)
CO2_rate = find_rate_p2(my_input, 0)

part2 = int(O2_rate, 2) * int(CO2_rate, 2)

print(str(part1) + " " + str(part2))

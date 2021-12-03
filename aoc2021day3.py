with open('C:/Users/User/Documents/input.txt') as f:
    my_input = f.read().split('\n')
f.close()


def invert_int(n):
    return ~n & (2 ** n.bit_length()) - 1


def resolve_needed_bits(numbers, flag, equal_check):
    count = []
    for bit_num in range(0, len(numbers[0]), 1):
        ones_input = list(filter(lambda num: num[bit_num] == '1', numbers))
        count.append(str(len(ones_input)))
    if equal_check:
        return "".join([str(flag) if float(flag_count) >= len(numbers) / 2 else str(~flag + 2) for flag_count in count])
    else:
        return "".join([str(flag) if float(flag_count) > len(numbers) / 2 else str(~flag + 2) for flag_count in count])


def find_last_num(numbers, flag, equal_check):
    for bit_num in range(0, len(numbers[0]), 1):
        check = resolve_needed_bits(numbers, flag, equal_check)
        numbers = [num for num in numbers if check[bit_num] == num[bit_num]]
        if len(numbers) == 1:
            return numbers[0]


gamma_rate = int(resolve_needed_bits(my_input, 1, False), 2)
epsilon_rate = invert_int(gamma_rate)
part1 = gamma_rate * epsilon_rate

O2_rate = find_last_num(my_input, 1, True)
CO2_rate = find_last_num(my_input, 0, True)

part2 = int(O2_rate, 2) * int(CO2_rate, 2)

print(str(part1) + " " + str(part2))

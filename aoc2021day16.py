import math
import re

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: re.findall(r'[A-Z]|\d', a), f.read()))
    my_input = [bin(int(i[0], 16)).split("b")[1] for i in my_input]
    my_input = "".join(['0'*(4-len(i)) + i for i in my_input])
f.close()


def unpack_sub(message):
    ver = int(message[0:3], 2)
    gr_type = message[6]
    gr_num = message[7:11]
    last_bit = 11
    while gr_type != '0':
        gr_type = message[last_bit]
        gr_num += message[last_bit + 1: last_bit + 5]
        last_bit += 5
    return ver, last_bit, int(gr_num, 2)


def op_pack_calc(type_id, nums):
    match type_id:
        case 0:
            return sum(nums)
        case 1:
            return math.prod(nums)
        case 2:
            return min(nums)
        case 3:
            return max(nums)
        case 5:
            return 1 if nums[0] > nums[1] else 0
        case 6:
            return 1 if nums[0] < nums[1] else 0
        case 7:
            return 1 if nums[0] == nums[1] else 0


def parse_packet(message):
    ver = int(message[0:3], 2)
    type_id = int(message[3:6], 2)
    if type_id == 4:
        gr_type = message[6]
        gr_num = message[7:11]
        last_bit = 11
        while gr_type != '0':
            gr_type = message[last_bit]
            gr_num += message[last_bit + 1: last_bit + 5]
            last_bit += 5
        message = message[last_bit:]
        gr_num = int(gr_num, 2)
    else:
        len_type_id = message[6]
        if len_type_id == '0':
            total_length = int(message[7:22], 2)
            sub = message[22:22 + total_length]
            ver += parse_packet(sub)
            message = message[22 + total_length:]
        else:
            ver += parse_packet(message[18:])
            return ver
    if message == '' or message.count('0') == len(message):
        return ver
    return ver + parse_packet(message)


part1 = parse_packet(my_input)


def parse_packet_p2(message):
    ver = int(message[0:3], 2)
    type_id = int(message[3:6], 2)
    if type_id == 4:
        gr_type = message[6]
        gr_num = message[7:11]
        last_bit = 11
        while gr_type != '0':
            gr_type = message[last_bit]
            gr_num += message[last_bit + 1: last_bit + 5]
            last_bit += 5
        message = message[last_bit:]
    else:
        len_type_id = message[6]
        total_length = int(message[7:22], 2) if len_type_id == '0' else int(message[7:18], 2)
        message = message[22:] if len_type_id == '0' else message[18:]
        nums = []
        while total_length > 0:
            ver_sub, last_bit, num = unpack_sub(message)
            nums.append(num)
            message = message[last_bit:]
            ver += ver_sub
            total_length -= last_bit if len_type_id == '0' else 1
        return ver, op_pack_calc(type_id, nums)
    if message == '' or message.count('0') == len(message):
        return ver, gr_num
    parsed = parse_packet(message)
    return ver + parsed[0], parsed[1]


part2 = parse_packet_p2(my_input)[1]

print(str(part1) + " " + str(part2))

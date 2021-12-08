import re

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(map(lambda b: re.findall(r'[a-z]+', b), a.split("|"))), f.read().split('\n')))
f.close()

part1 = len([digit for line in my_input for digit in line[1] if len(digit) < 5 or len(digit) > 6])

part2 = 0
for line in my_input:
    number = ""
    patterns = {}
    display = {}
    for digit in line[0]:
        match len(digit):
            case 2:
                patterns[1] = digit
            case 3:
                patterns[7] = digit
            case 4:
                patterns[4] = digit
            case 7:
                patterns[8] = digit
    display['up r'] = patterns[1]
    display['down r'] = patterns[1]
    display['up l'] = [c for c in patterns[4] if c not in patterns[1]]
    display['mid'] = [c for c in patterns[4] if c not in patterns[1]]
    display['down l'] = [c for c in patterns[8] if c not in patterns[7] and c not in patterns[4]]
    display['down'] = [c for c in patterns[8] if c not in patterns[7] and c not in patterns[4]]
    digits = [d for d in line[0] if len(d) == 6]
    for digit in digits:
        if len(display['mid']) > 1 and (display['mid'][0] not in digit or display['mid'][1] not in digit):
            display['mid'] = display['mid'][0] if display['mid'][0] not in digit else display['mid'][1]
            display['up l'] = [d for d in display['up l'] if d not in display['mid']][0]
            patterns[0] = digit
        if len(display['down l']) > 1 and (display['down l'][0] not in digit or display['down l'][1] not in digit):
            display['down l'] = display['down l'][0] if display['down l'][0] not in digit else display['down l'][1]
            display['down'] = [d for d in display['down'] if d not in display['down l']][0]
            patterns[9] = digit
    patterns[6] = [d for d in digits if d != patterns[0] and d != patterns[9]][0]
    display['up r'] = display['up r'][0] if display['up r'][0] not in patterns[6] else display['up r'][1]
    display['down r'] = [d for d in display['down r'] if d not in display['up r']][0]
    digits = [d for d in line[0] if len(d) == 5]
    for digit in digits:
        if display['up l'] not in digit and display['down r']not in digit:
            patterns[2] = digit
        if display['down l'] not in digit and display['up r'] not in digit:
            patterns[5] = digit
        if display['down l'] not in digit and display['up l'] not in digit:
            patterns[3] = digit
    for digit in line[1]:
        for dig, pat in patterns.items():
            if len(digit) == len(pat) and len([ch for ch in pat if ch not in digit]) == 0:
                number += str(dig)
                break
    part2 += int(number)

print(str(part1) + " " + str(part2))

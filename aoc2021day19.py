import re

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = f.read().split('\n\n')
f.close()

scanners = {re.findall(r'\d+', scanner.split('\n')[0])[0]:
                [list(map(lambda a: int(a), re.findall(r'-?\d+', coords))) for i, coords in enumerate(scanner.split('\n')) if i != 0]
            for scanner in my_input}



part1 = 0
part2 = 0

print(str(part1) + ' ' + str(part2))

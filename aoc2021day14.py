with open('C:/Users/User/Documents/input.txt') as f:
    my_input = f.read().split('\n\n')
f.close()

template = my_input[0]
rules = {line.split(' -> ')[0]:line.split(' -> ')[1] for line in my_input[1].split('\n')}

cur_str = template
for i in range(1, 11):
    new_str = 'a'
    for pos in range(0, len(cur_str)-1):
        new_str = new_str[:-1]
        new_str += cur_str[pos] + rules[cur_str[pos:pos+2]] + cur_str[pos+1]
    cur_str = new_str

uniq = {k:cur_str.count(k) for k in cur_str}
part1 = max(uniq.values()) - min(uniq.values())

part2 = 0

print(str(part1) + " " + str(part2))

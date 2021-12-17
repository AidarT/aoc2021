import re

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: list(map(lambda b: int(b), re.findall(r'-?\d+', a))), f.read().split('\n')))[0]
f.close()


def calc_path(constrains, start, vel, y_max):
    drag_x = 0 if vel[0] == 0 else 1 if vel[0] < 0 else -1
    new_pos = [start[0] + vel[0], start[1] + vel[1]]
    vel[0] += drag_x
    vel[1] -= 1
    y_max = new_pos[1] if y_max < new_pos[1] else y_max
    if constrains[0] <= new_pos[0] <= constrains[1] and constrains[2] <= new_pos[1] <= constrains[3]:
        return True, new_pos, y_max
    if new_pos[0] > constrains[1] or new_pos[1] < constrains[2]:
        return False, new_pos, y_max
    return calc_path(constrains, new_pos, vel, y_max)


vel = [0, my_input[2]]
solutions = []
last_flag = []
change_x = False
while True:
    flag, pos, y_max = calc_path(my_input, [0, 0], vel.copy(), -999)
    if flag:
        solutions.append([vel.copy(), pos.copy(), y_max])
    last_flag.append(flag)
    if last_flag.count(False) >= my_input[1]:
        change_x = True
        last_flag.clear()
    if not change_x:
        vel[1] += 1
    else:
        change_x = False
        vel[1] = my_input[2]
        vel[0] += 1
    if vel[0] > my_input[1]:
        break

part1 = max([sol[2] for sol in solutions])
part2 = len(solutions)

print(str(part1) + ' ' + str(part2))

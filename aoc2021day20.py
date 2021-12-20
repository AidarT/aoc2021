with open('C:/Users/User/Documents/input.txt') as f:
    alg, pic = f.read().split('\n\n')
f.close()

pic = pic.split('\n')


def calc_pixel(i, j, pic, alg):
    num = pic[j-1][i-1:i+2] + pic[j][i-1:i+2] + pic[j+1][i-1:i+2]
    num = num.replace('.', '0').replace('#', '1')
    return alg[int(num, 2)]


def output_pic(pic, alg):
    new_pic = []
    for j in range(1, len(pic) - 1):
        new_pic.append('')
        for i in range(1, len(pic[0]) - 1):
            new_pic[-1] += calc_pixel(i, j, pic, alg)
    return new_pic


def pre_enhance(pic):
    pic = ['.' * 5 + line + '.' * 5 for line in pic]
    pic = ['.' * len(pic[0]) for i in range(5)] + pic + ['.' * len(pic[0]) for i in range(5)]
    return pic


def cycle(pic, alg, amount):
    for i in range(amount):
        pic = pre_enhance(pic.copy())
        pic = output_pic(pic.copy(), alg)
    pic_cut = pic[3 * (i + 1):-3 * (i + 1)]
    pic_cut = [line[3 * (i + 1):-3 * (i + 1)] for line in pic_cut]
    for line in pic:
        print(line)
    return sum([sum(1 for ch in line if ch == '#') for line in pic_cut])


part1 = cycle(pic, alg, 2)
part2 = cycle(pic, alg, 50)

print(str(part1) + ' ' + str(part2))

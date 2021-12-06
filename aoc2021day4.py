import math
import re
from functools import reduce

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = f.read().split('\n')
f.close()

order = [int(num) for num in my_input[0].split(",")]
boards, marks = {}, {}
start = 2
boards_amount = math.floor((len(my_input) - 2) / 5)
for i in range(0, boards_amount):
    boards[i] = my_input[start:start + 5]
    marks[i] = [[1 for num in re.findall(r'\d+', line)] for line in boards[i]]
    boards[i] = [[int(num) for num in re.findall(r'\d+', line)] for line in boards[i]]
    start += 6


def cal_win(board, mark, num):
    board_lined = [e for l in board for e in l]
    mark_lined = [e for l in mark for e in l]
    return num * reduce(lambda prev, cur: prev + cur[1] * mark_lined[cur[0]], enumerate(board_lined), 0)


def bingo(order, boards, marks):
    for num in order:
        for i in range(0, boards_amount):
            for j, line in enumerate(boards[i]):
                count = line.count(num)
                while count > 0:
                    index = line.index(num)
                    marks[i][j][index] = 0
                    count -= 1
                    win = marks[i][j].count(0)
                    if win == 5:
                        return cal_win(boards[i], marks[i], num)
                    column = [num[index] for num in marks[i]]
                    win = column.count(0)
                    if win == 5:
                        return cal_win(boards[i], marks[i], num)


part1 = bingo(order, boards, marks.copy())


def find_last(order, boards, marks):
    win_boards = [0 for i in range(0, boards_amount)]
    last = 0
    last_num = 0
    for num in order:
        for i in range(0, boards_amount):
            if win_boards[i] == 0:
                for j, line in enumerate(boards[i]):
                    count = line.count(num)
                    while count > 0:
                        index = line.index(num)
                        marks[i][j][index] = 0
                        count -= 1
                        win = marks[i][j].count(0)
                        if win == 5:
                            if win_boards.count(0) > 1:
                                win_boards[i] = 1
                                last = i
                                last_num = num
                                break
                            else:
                                return cal_win(boards[i], marks[i], num)
                        column = [num[index] for num in marks[i]]
                        win = column.count(0)
                        if win == 5:
                            if win_boards.count(0) > 1:
                                win_boards[i] = 1
                                last = i
                                last_num = num
                                break
                            else:
                                return cal_win(boards[i], marks[i], num)
                    if win_boards[i] == 1:
                        break
    return cal_win(boards[last], marks[last], last_num)


part2 = find_last(order, boards, marks.copy())

print(str(part1) + " " + str(part2))

from itertools import pairwise, tee


def part_one_solution(lines):
    total = len([1 for curr, next in pairwise(lines) if int(curr) < int(next)])
    print(total)


def part_two_solution(lines):
    lines = [int(x) for x in lines]
    i = 0
    for x in range(len(lines)):
        if sum(lines[x : x + 3]) < sum(lines[x + 1 : x + 4]):
            i += 1
    print(i)


with open("./input.txt") as f:
    lines = f.readlines()
    part_one_solution(lines)
    part_two_solution(lines)

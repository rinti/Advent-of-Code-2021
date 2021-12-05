from collections import defaultdict


def part_one_solution(dict):
    forward = dict["forward"]
    depth = dict["down"] - dict["up"]

    print(forward * depth)


def part_two_solution(dict):
    print(abs(dict["forward"] * dict["depth"]))


with open("./input.txt") as f:
    dict = defaultdict(int)
    dict["aim"] = 0
    dict["depth"] = 0

    for line in f.readlines():
        dir, amount = line.split(" ")
        dict[dir] += int(amount)
        if dir == "forward":
            dict["depth"] += (dict["down"] - dict["up"]) * int(amount)

    part_one_solution(dict)
    part_two_solution(dict)

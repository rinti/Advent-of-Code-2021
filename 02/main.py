from collections import defaultdict

with open("./input.txt") as f:
    dict = defaultdict(int)
    for line in f.readlines():
        dir, amount = line.split(" ")
        dict[dir] += int(amount)

    forward = dict["forward"]
    depth = dict["down"] - dict["up"]

    print(forward * depth)

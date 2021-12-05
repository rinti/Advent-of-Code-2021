from itertools import pairwise

with open("./input.txt") as f:
    i = 0
    for curr, next in pairwise(f.readlines()):
        if int(curr) < int(next):
            i += 1
    print(i)

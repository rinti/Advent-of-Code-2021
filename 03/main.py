from collections import defaultdict


def get_gamma_and_epsilon(dicts):
    gamma = ""
    epsilon = ""
    for x in dicts:
        if x["1"] > x["0"]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return gamma, epsilon


with open("./input.txt") as f:
    lines = f.readlines()

    dicts = [defaultdict(int) for _ in range(12)]

    for line in lines:
        line = line.strip()
        for i, number in enumerate(line):
            dicts[i][number] += 1

    gamma, epsilon = get_gamma_and_epsilon(dicts)
    print(int(gamma, 2) * int(epsilon, 2))

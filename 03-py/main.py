from collections import defaultdict


def count_bits(lines):
    dicts = [defaultdict(int) for _ in range(12)]

    for line in lines:
        line = line.strip()
        for i, number in enumerate(line):
            dicts[i][number] += 1

    return dicts


def get_gamma_and_epsilon(lines):
    dicts = count_bits(lines)
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


def part_one_solution(lines):
    gamma, epsilon = get_gamma_and_epsilon(lines)
    print(int(gamma, 2) * int(epsilon, 2))


def part_two_solution(lines):
    def get_rating(lines, bit=0, type="oxygen"):
        dicts = count_bits(lines)

        if type == "oxygen":
            comparator = dicts[bit]["1"] >= dicts[bit]["0"]
        else:
            comparator = dicts[bit]["1"] < dicts[bit]["0"]

        if comparator:
            lines = [x for x in lines if x[bit] == "1"]
        else:
            lines = [x for x in lines if x[bit] == "0"]

        if len(lines) > 1:
            return get_rating(lines, bit + 1, type)
        else:
            return lines[0].strip()

    oxygen_rating = get_rating(lines)
    co2_scrubber_rating = get_rating(lines, type="co2")

    print(int(oxygen_rating, 2) * int(co2_scrubber_rating, 2))


with open("./input.txt") as f:
    lines = f.readlines()

    part_one_solution(lines)
    part_two_solution(lines)

from utils.file_reader import read_file_to_lines
from itertools import permutations
from collections import Counter


def data_prep(instructions):
    data = dict()
    for x, line in enumerate(instructions):
        for y, column in enumerate(line):
            data[(x, y)] = int(column)
    return data


def flash(data, flashed):
    offsets = list(set(permutations([-1, -1, 0, 1, 1], 2)))
    for co, value in data.items():
        if value < 10 or co in flashed:
            continue
        flashed.append(co)
        for offset in offsets:
            n_co = (co[0] + offset[0], co[1] + offset[1])
            neighbor = data.get(n_co, None)
            if neighbor is None or n_co in flashed:
                continue
            data[n_co] += 1
            if data[n_co] > 9:
                data, flashed = flash(data, flashed)
    return data, flashed


def step(data):
    flashed = list()
    data = {x: y + 1 for x, y in data.items()}
    data, flashed = flash(data, flashed)
    flashes = len(flashed)
    for x, y in data.items():
        if y > 9:
            data[x] = 0
    return data, flashes


def part_one(data):
    flashes = 0
    for _ in range(100):
        data, new_flashes = step(data)
        flashes += new_flashes
    return flashes


def part_two(data):
    count = 1
    while True:
        data, _ = step(data)
        if Counter(data.values())[0] == len(data.items()):
            break
        count += 1
    return count


def main():
    file_path = "inputs/day_11.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))  # 1725
    print(part_two(data))  # 308


if __name__ == "__main__":
    main()

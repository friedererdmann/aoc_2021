import sys
from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    data = [int(x) for x in instructions[0].split(",")]
    # print(sum(data), len(data))
    return data


def part_one(instructions):
    minimum = sys.maxsize
    point = 0
    for i in range(max(instructions)):
        distance = sum([abs(x - i) for x in instructions])
        if distance < minimum:
            minimum = distance
            point = i
    return point, minimum


def part_two(instructions):
    max_distance = sys.maxsize
    point = 0
    for i in range(max(instructions)):
        distance = 0
        for j in instructions:
            x = abs(i - j)
            distance += (x * x + x) / 2
        if distance < max_distance:
            max_distance = distance
            point = i
    return point, max_distance


def main():
    file_path = "inputs/day_07.txt"
    instructions = read_file_to_lines(file_path)
    instructions = ["16,1,2,0,4,2,7,1,2,14"]
    data = data_prep(instructions)
    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()

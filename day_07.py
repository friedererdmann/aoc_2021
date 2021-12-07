import sys
from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    data = [int(x) for x in instructions[0].split(",")]
    return data


def part_one(data):
    minimum = sys.maxsize
    for i in range(max(data)):
        minimum = min(minimum, sum([abs(x - i) for x in data]))
    return minimum


def part_two(data):
    minimum = sys.maxsize
    for i in range(max(data)):
        minimum = min(minimum, sum([(((x - i) ** 2) + abs(x - i)) // 2 for x in data]))
    return minimum


def main():
    file_path = "inputs/day_07.txt"
    instructions = read_file_to_lines(file_path)
    # instructions = ["16,1,2,0,4,2,7,1,2,14"]
    data = data_prep(instructions)
    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()

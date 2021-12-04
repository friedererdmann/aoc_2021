from utils.file_reader import read_file_to_lines
from operator import lt, ge


def part_one(instructions):
    gamma = int(most_common_bit(instructions), 2)
    epsilon = pow(2, len(instructions[0])) - 1 - gamma
    return gamma * epsilon


def part_two(instructions):
    oxygen = int(deduce(instructions), 2)
    carbon = int(deduce(instructions, lt), 2)
    return oxygen * carbon


def most_common_bit(instructions, comp=ge):
    transpose = list(zip(*instructions))
    common_bits = "".join([str(int(comp(row.count("1"), (len(row) / 2)))) for row in transpose])
    return common_bits


def deduce(instructions, comp=ge):
    length = len(instructions[0])
    for idx in range(length):
        o_idx = most_common_bit(instructions, comp)[idx]
        instructions = [line for line in instructions if line[idx] == o_idx]
        if len(instructions) == 1:
            return instructions[0]


def main():
    file_path = "inputs/day_03.txt"
    instructions = read_file_to_lines(file_path)
    print(part_one(instructions))  # 4006064 # 198
    print(part_two(instructions))  # 5941884 # 230


if __name__ == "__main__":
    main()

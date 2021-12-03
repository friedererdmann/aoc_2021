from typing import Counter, Union
from utils.file_reader import read_file_to_lines


def part_one(instructions):
    transpose = list(map(list, zip(*instructions)))
    gamma = "".join([max(set(row), key=row.count) for row in transpose])
    epsilon = "".join([min(set(row), key=row.count) for row in transpose])

    return int(gamma, 2) * int(epsilon, 2)


def part_two(instructions):
    transpose = list(map(list, zip(*instructions)))
    oxygen_lines = list(range(len(instructions)))
    scrubbing_lines = list(range(len(instructions)))
    oxygen_rate = ""
    scrubber_rate = ""
    lines = instructions
    for idx, row in enumerate(transpose):
        oxygen_valid_rows = [row[i] for i in oxygen_lines]
        scrubbing_valid_rows = [row[i] for i in scrubbing_lines]
        o_count = oxygen_valid_rows.count("1") - oxygen_valid_rows.count("0")
        s_count = scrubbing_valid_rows.count("1") - scrubbing_valid_rows.count("0")
        o_bit = str(int(o_count >= 0))
        s_bit = str(int(s_count < 0))
        oxygen_lines = [i for i, line in enumerate(lines) if line[idx] == o_bit and i in oxygen_lines]
        scrubbing_lines = [i for i, line in enumerate(lines) if line[idx] == s_bit and i in scrubbing_lines]
        if len(oxygen_lines) == 1:
            oxygen_rate = instructions[oxygen_lines[0]]
        if len(scrubbing_lines) == 1:
            scrubber_rate = instructions[scrubbing_lines[0]]

    return int(oxygen_rate, base=2) * int(scrubber_rate, base=2)


def main():
    file_path = "inputs/day_03.txt"
    instructions = read_file_to_lines(file_path)
    print(part_one(instructions))  # 4006064
    print(part_two(instructions))  # 5941884


if __name__ == "__main__":
    main()

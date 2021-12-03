from typing import Counter, Union
from itertools import accumulate
from functools import reduce
from utils.file_reader import read_file_to_lines
from operator import mul, add


def part_one(instructions):
    gamma = most_common_bit(instructions, "1")
    epsilon = ~ gamma & pow(2, len(instructions[0])) - 1  # flip the bits and
    return gamma * epsilon


def part_two(instructions):
    transpose = list(zip(*instructions))
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


def most_common_bit(instructions, bit="1"):
    """Each bit in the gamma rate can be determined by finding the most common
    bit in the corresponding position of all numbers in the diagnostic report.
    Find the most common number in each column of the original data"""
    transpose = list(zip(*instructions))
    common_bits = int("".join([str(int(row.count(bit) > (len(row) / 2))) for row in transpose]), 2)
    # rows in transpose were columns in the original data
    # by counting the occurence of "1" and seeing if its more than half the entries
    # we can safely say if it is the most common bit or zero
    return common_bits


def main():
    file_path = "inputs/day_03.txt"
    instructions = ["00100",
                    "11110",
                    "10110",
                    "10111",
                    "10101",
                    "01111",
                    "00111",
                    "11100",
                    "10000",
                    "11001",
                    "00010",
                    "01010"]
    instructions = read_file_to_lines(file_path)
    print(part_one(instructions))  # 4006064 # 198
    print(part_two(instructions))  # 5941884 # 230


if __name__ == "__main__":
    main()

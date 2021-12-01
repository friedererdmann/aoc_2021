# from utils import file_reader
from typing import List
from itertools import pairwise


def part_one(meassures: List[int]) -> int:
    return sum([i < j for i, j in pairwise(meassures)])


def part_two(meassures: List[int], window: int = 3) -> int:
    return part_one([sum(meassures[i : i + window]) for i in range(len(meassures))])


def main():
    file_path = "inputs/day_01.txt"

    input_list: List[int]

    with open(file_path, 'r') as file_handler:
        input_list = [int(i) for i in file_handler.readlines()]

    print(part_one(input_list))
    print(part_two(input_list, 3))


if __name__ == "__main__":
    main()

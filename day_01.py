from typing import List
from itertools import pairwise
from utils.file_reader import get_list_of_ints_from_file


def part_one(in_list: List[int]) -> int:
    return sum([i < j for i, j in pairwise(in_list)])


def part_two(in_list: List[int], avg: int = 3) -> int:
    return part_one([sum(in_list[i: i + avg]) for i in range(len(in_list))])


def main():
    file_path = "inputs/day_01.txt"

    input_list = get_list_of_ints_from_file(file_path)

    print(part_one(input_list))
    print(part_two(input_list, 3))


if __name__ == "__main__":
    main()

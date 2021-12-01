# from utils import file_reader
from typing import List


def part_one(depth_meassures: List[int]) -> int:
    increase = 0

    for i, meassure in enumerate(depth_meassures):
        if not i:
            continue
        prev = depth_meassures[i - 1]
        if meassure > prev:
            increase += 1

    return increase


def part_two(depth_meassures: List[int], window_size: int = 3) -> int:
    averaged = list()
    for i in range(len(depth_meassures)):
        if i + window_size <= len(depth_meassures):
            averaged.append(sum(depth_meassures[i:i + window_size]))

    increase = part_one(averaged)

    return increase

file_path = "inputs/day_01.txt"

input_list: List[int]

with open(file_path, 'r') as file_handler:
    input_list = [int(i) for i in file_handler.readlines()]

print(part_one(input_list))
print(part_two(input_list))

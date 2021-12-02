from utils.file_reader import read_file_to_lines


def part_one(in_list):
    horizontal = 0
    vertical = 0

    h = ["forward"]
    v = ["down", "up"]

    for inst in instructions:
        direction, amount = inst.split()
        if direction in h:
            horizontal += int(amount)
        if direction == "down":
            vertical += int(amount)
        if direction == "up":
            vertical -= int(amount)

    return horizontal * vertical


def part_two(in_list):
    horizontal = 0
    vertical = 0
    aim = 0

    for inst in instructions:
        direction, amount = inst.split()
        if direction in h:
            horizontal += int(amount)
            vertical += aim * int(amount)
        if direction == "down":
            aim += int(amount)
        if direction == "up":
            aim -= int(amount)

    return horizontal * vertical


file_path = "inputs/day_02.txt"
instructions = read_file_to_lines(file_path)
print(part_one)
print(part_two)

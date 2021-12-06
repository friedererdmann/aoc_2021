from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    start_list = [int(x) for x in instructions[0].split(",")]
    start_dict = {}
    for i in range(9):
        start_dict[i] = start_list.count(i)
    print(start_dict)
    return start_dict


def looping(instructions):
    new_instructions = {k-1: v for k, v in instructions.items() if k >= 0}
    respawn = new_instructions.get(-1, 0)
    if respawn:
        new_instructions[8] = respawn
        if 6 in new_instructions:
            new_instructions[6] += respawn
        else:
            new_instructions[6] = respawn
    return {k: v for k, v in new_instructions.items() if k >= 0}


def part_one(instructions):
    for day in range(80):
        instructions = looping(instructions)
    return sum(instructions.values())


def part_two(instructions):
    for i in range(256):
        instructions = looping(instructions)
    return sum(instructions.values())


def main():
    file_path = "inputs/day_06.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))  # 352872
    print(part_two(data))  # 1604361182149


if __name__ == "__main__":
    main()

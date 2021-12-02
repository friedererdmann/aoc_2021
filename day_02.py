from utils.file_reader import read_file_to_lines


def part_one(f_list):
    horizontal = 0
    vertical = 0

    for i, j in f_list:
        horizontal += i
        vertical += j
    return horizontal * vertical


def part_two(f_list):
    horizontal = 0
    vertical = 0
    aim = 0

    for i, j in f_list:
        vertical += aim * i
        horizontal += i
        aim += j

    return horizontal * vertical


def data_prep(lines):
    fwd = "forward"
    dwn = "down"
    up = "up"
    vector_list = [(int(value_) * (dir_ == fwd), int(value_) * ((dir_ == dwn) - (dir_ == up))) for (dir_, value_) in [i.split() for i in lines]]
    return vector_list


def main():
    file_path = "inputs/day_02.txt"
    instructions = read_file_to_lines(file_path)
    formatted_inst = data_prep(instructions)
    print(part_one(formatted_inst))  # 1938402
    print(part_two(formatted_inst))  # 1947878632


if __name__ == "__main__":
    main()

from utils.file_reader import read_file_to_lines


def part_one(f_list):
    horizontal = 0
    vertical = 0

    fwd = "forward"
    dwn = "down"
    up = "up"

    for dir_, value_ in f_list:
        horizontal += value_ * (dir_ == fwd)
        vertical += value_ * ((dir_ == dwn) - (dir_ == up))

    return horizontal * vertical


def part_two(f_list):
    horizontal = 0
    vertical = 0
    aim = 0

    fwd = "forward"
    dwn = "down"
    up = "up"

    for dir_, value_ in f_list:
        vertical += aim * value_ * (dir_ == fwd)
        horizontal += value_ * (dir_ == fwd)
        aim += value_ * ((dir_ == dwn) - (dir_ == up))

    return horizontal * vertical


def data_prep(lines):
    fwd = "forward"
    dwn = "down"
    up = "up"
    vector_list = [(int(value_) * (dir_ == fwd), int(value_) * ((dir_ == dwn) - (dir_ == up))) for (dir_, value_) in [i.split() for i in lines]]
    # print(vector_list)
    formatted_inst = [(x, int(y)) for (x, y) in [i.split() for i in lines]]
    return formatted_inst


def main():
    file_path = "inputs/day_02.txt"
    instructions = read_file_to_lines(file_path)
    formatted_inst = data_prep(instructions)
    print(part_one(formatted_inst))  # 1938402
    print(part_two(formatted_inst))  # 1947878632


if __name__ == "__main__":
    main()

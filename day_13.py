from collections import defaultdict
from utils.file_reader import read_file_to_lines


def data_prep(instructions):
    dots = list()
    rest = 0
    for i, line in enumerate(instructions):
        if not line:
            rest = i
            break
        dots.append([int(x) for x in line.split(",")])
    folds = [x[11:].split("=") for x in instructions[rest+1:]]
    data = [dots, folds]
    return data


def part_one(data):
    dots = data[0]
    folds = data[1]
    max_x = max([x[0] for x in dots])
    max_y = max([x[1] for x in dots])
    for axis, line in folds[:1]:
        line = int(line)
        new_dots = list()
        for dot in dots:
            if axis == "y":
                max_y = line
                if dot[1] < line:
                    new_dots.append(dot)
                if dot[1] > line:
                    new_dot = [dot[0], line * 2 - dot[1]]
                    new_dots.append(new_dot)
            if axis == "x":
                max_x = line
                if dot[0] < line:
                    new_dots.append(dot)
                if dot[0] > line:
                    new_dot = [line * 2 - dot[0], dot[1]]
                    new_dots.append(new_dot)
        dots = new_dots
    dictionary = dict()
    for dot in dots:
        dictionary[(dot[0], dot[1])] = "#"
    return len(dictionary.values())


def part_one(data):
    dots = data[0]
    folds = data[1]
    max_x = max([x[0] for x in dots])
    max_y = max([x[1] for x in dots])
    for axis, line in folds:
        line = int(line)
        new_dots = list()
        for dot in dots:
            if axis == "y":
                max_y = line
                if dot[1] < line:
                    new_dots.append(dot)
                if dot[1] > line:
                    new_dot = [dot[0], line * 2 - dot[1]]
                    new_dots.append(new_dot)
            if axis == "x":
                max_x = line
                if dot[0] < line:
                    new_dots.append(dot)
                if dot[0] > line:
                    new_dot = [line * 2 - dot[0], dot[1]]
                    new_dots.append(new_dot)
        dots = new_dots
    dictionary = dict()
    for dot in dots:
        dictionary[(dot[0], dot[1])] = "#"
    for y in range(max_y):
        new_line = ""
        for x in range(max_x):
            new_line += dictionary.get((x,y), ".")
        print(new_line)
    return


def main():
    file_path = "inputs/day_13.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))  # 1725
    print(part_two(data))  # 308


if __name__ == "__main__":
    main()

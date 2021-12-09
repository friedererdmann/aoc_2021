from utils.file_reader import read_file_to_lines
from collections import defaultdict


def data_prep(instructions):
    data = dict()
    for x, line in enumerate(instructions):
        for y, column in enumerate(line):
            data[(x,y)] = int(column)
    return data


def part_one(data):
    minima = list()
    for coordinate, value in data.items():
        smallest = True
        for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
            comparison = data.get((coordinate[0] + direction[0], coordinate[1] + direction[1]), None)
            if comparison != None:
                if value >= comparison:
                    smallest = False
                    break
        if smallest:
            minima.append(value)
    return sum([x+1 for x in minima])


def gradient_ascent(coordinate, value, data):
    coordinates = list()
    coordinates.append(coordinate)
    for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
        co_cordinate = (coordinate[0] + direction[0], coordinate[1] + direction[1])
        comparison = data.get(co_cordinate, None)
        if comparison != None:
            if comparison > value and comparison != 9:
                for each in gradient_ascent(co_cordinate, comparison, data):
                    coordinates.append(each)
    return coordinates


def part_two(data):
    minima = list()
    for coordinate, value in data.items():
        smallest = True
        for direction in [(-1,0),(1,0),(0,1),(0,-1)]:
            comparison = data.get((coordinate[0] + direction[0], coordinate[1] + direction[1]), None)
            if comparison != None:
                if value >= comparison:
                    smallest = False
                    break
        if smallest:
            minima.append((coordinate, value))

    coordinates = list()
    for coordinate, value in minima:
        coordinates.append(set(gradient_ascent(coordinate, value, data)))

    coordinates.sort(key=len)
    size = 1
    for x in coordinates[-3:]:
        size *= len(x)

    return size


def main():
    file_path = "inputs/day_09.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))  # 491
    print(part_two(data))  # 1075536


if __name__ == "__main__":
    main()

from collections import Counter
from utils.file_reader import read_file_to_lines

START = "start"
END = "end"


def data_prep(instructions):
    data = [x.split("-") for x in instructions]
    return data


def xforward(data, start, paths=None, full_path="", visited=None):
    all_paths = list()
    full_path += start + ","
    if not paths:
        paths = list()
    if not visited:
        visited = list()
    possibilities = [path for path in data if start in path]
    for path in possibilities:

        next = 1 - path.index(start)
        direction = [start, path[next]]
        if path[next] == END:
            # print(full_path + END)
            all_paths.append(full_path + END)
        elif direction not in paths:
            if direction[1] not in visited:
                if direction[1].islower() and direction[1] in full_path:
                    continue
                paths.append(direction)
                if start.islower():
                    visited.append(start)

                all_paths += forward(data, path[next], paths, full_path, visited)
                if visited:
                    visited.pop(-1)
                if paths:
                    paths.pop(-1)

    return all_paths

def forward(data, start, paths=None, full_path=None, visited=None):
    all_paths = list()
    if not full_path:
        full_path = list()
    full_path.append(start)
    if not paths:
        paths = list()
    if not visited:
        visited = list()
    possibilities = [path for path in data if start in path]
    for path in possibilities:
        next = 1 - path.index(start)
        direction = [start, path[next]]
        if path[next] == END:
            print(full_path, END)
            all_paths.append(full_path)
        elif direction not in paths:
            
            if direction[1] not in visited:
                if direction[1].islower() and direction[1] in full_path:
                    continue
                paths.append(direction)
                if start.islower():
                    visited.append(start)
                
                all_paths += forward(data, path[next], paths, full_path, visited)
                if visited:
                    visited.pop(-1)
                if paths:
                    paths.pop(-1)
                if full_path:
                    full_path.pop(-1)

    return all_paths


def forward_two(data, start, paths=None, full_path=None, visited=None, twice=False):
    all_paths = list()
    if not full_path:
        full_path = list()
    full_path.append(start)
    if not paths:
        paths = list()
    if not visited:
        visited = list()
    possibilities = [path for path in data if start in path]
    for path in possibilities:
        next = 1 - path.index(start)
        direction = [start, path[next]]
        if path[next] == END:
            print(full_path, END)
            all_paths.append(full_path)
        elif direction not in paths:
            if direction[1] not in visited:
                if direction[1] == START:
                    continue
                paths.append(direction)
                if start.islower() and twice:
                    print(twice)
                    visited.append(start)
                all_paths += forward_two(data, path[next], paths, full_path, visited, twice)
                if visited:
                    visited.pop(-1)
                if paths:
                    paths.pop(-1)
                if full_path:
                    full_path.pop(-1)

    return all_paths


def part_one(data):
    paths = forward(data, START)
    return len(paths)


def part_two(data):
    paths = forward_two(data, START)
    return len(paths)


def main():
    file_path = "inputs/day_12.txt"
    instructions = read_file_to_lines(file_path)
    data = data_prep(instructions)
    print(part_one(data))  # 4549
    print(part_two(data))


if __name__ == "__main__":
    main()
